from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    # URL для входа
    path("", index),
    path("ex_ussr_c/", ex_ussr),
]