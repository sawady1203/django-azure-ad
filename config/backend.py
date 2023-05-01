from mozilla_django_oidc.auth import OIDCAuthenticationBackend

class MyOIDCAB(OIDCAuthenticationBackend):
    def _get_email_from_claims(self, claims):
        # claims に emails でしか返ってこない場合はここをカスタムする
        email = claims.get('email', '')

        return email

    def create_user(self, claims):
        user = super(MyOIDCAB, self).create_user(claims)
        user.email = self._get_email_from_claims(claims)
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        return user

    def update_user(self, user, claims):
        user.email = self._get_email_from_claims(claims)
        user.first_name = claims.get('given_name', '')
        user.last_name = claims.get('family_name', '')
        user.save()

        return user
