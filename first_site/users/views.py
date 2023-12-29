from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserRegistrationForm, ProfileForm, ChangePassword

from django.views.decorators.http import require_http_methods

from .services import update_user, change_password


def registration(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "registration/registration_succesfull.html", {"new_user": new_user})
    else:
        if request.user.is_authenticated:
            return render(request, "registration/registration.html", {"ask_logout": True})
        user_form = UserRegistrationForm()
        return render(request, "registration/registration.html", {"user_form": user_form})


def profile(request):
    profile_form = ProfileForm(initial={"username": request.user.username, "email": request.user.email})
    if request.method == "POST":
        password_form = ChangePassword(request.POST, user=request.user)
        if password_form.is_valid():
            change_password(request.user, password_form.cleaned_data["new_password"])
    else:
        password_form = ChangePassword(user=request.user)
    page_data = {"profile_form": profile_form, "password_form": password_form}
    return render(request, "registration/profile.html", page_data)

@require_http_methods(["POST"])
def profile_edit(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        update_user(request.user, form.cleaned_data["username"], form.cleaned_data["email"])
    return redirect(reverse("profile"))