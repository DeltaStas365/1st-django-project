from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
    path("profile/", profile, name='profile'),
    path("register/", registration, name="signup"),
    path("profile/edit", profile_edit, name="edit_profile"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)