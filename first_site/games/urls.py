from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    # URL для входа
    path("", main, name="main"),
    path("games/<int:id>/", game_page, name="game_page"),
    path("games/<int:id>/comment", add_comment, name="add_comment"),
    path("catergories/<int:id>/", category_page, name="category_page"),
    path("compilations/", compilations_page, name="compilations_page"),
    path("compilations/<int:id>/", compilation_page, name="compilation_page")
]