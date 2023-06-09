"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'mozilla_django_oidc',
    # Custom Apps
    'users.apps.UsersConfig',
    'sample.apps.SampleConfig',
]

AUTH_USER_MODEL = 'users.CustomUser'

# Add 'mozilla_django_oidc' authentication backend
AUTHENTICATION_BACKENDS = (
    # Azure AD でのログイン
    'config.backend.MyOIDCAB',
    # 'mozilla_django_oidc.auth.OIDCAuthenticationBackend',

    # djangoのID/Passでのログイン
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mozilla_django_oidc.middleware.SessionRefresh',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "sample:index"

# moziall-oidc-django settings for Azure AD
OIDC_RP_CLIENT_ID = os.getenv("AAD_OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = os.getenv("AAD_OIDC_RP_CLIENT_SECRET")
OIDC_RP_SIGN_ALGO = os.getenv("AAD_OIDC_RP_SIGN_ALGO", "RS256")
OIDC_OP_JWKS_ENDPOINT = os.getenv("AAD_OIDC_OP_JWKS_ENDPOINT")
OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv("AAD_OIDC_OP_AUTHORIZATION_ENDPOINT")
OIDC_OP_TOKEN_ENDPOINT = os.getenv("AAD_OIDC_OP_TOKEN_ENDPOIT")
OIDC_OP_USER_ENDPOINT = os.getenv("AAD_OIDC_OP_USER_ENDPOINT")
LOGOUT_REDIRECT_URL = os.getenv("AAD_LOGOUT_REDIRECT_URL")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'mozilla_django_oidc': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}