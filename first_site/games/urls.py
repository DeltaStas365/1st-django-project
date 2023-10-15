from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    # URL для входа
    path("", main, name="main"),
    path("games/<int:id>/", game_page, name="game_page")
]