from django.urls import path
from .views import *
urlpatterns = [
    path("profile/", profile),
    path("register/", registration),
]