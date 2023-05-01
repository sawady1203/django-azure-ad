from django.urls import path, include
from . import views

app_name = "sample"

urlpatterns = [
    path('', views.index, name="index"),
]
