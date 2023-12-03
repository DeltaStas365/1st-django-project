from django.shortcuts import render

from users.forms import UserRegistrationForm, ProfileForm


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
    page_data = {"profile_form": profile_form}
    return render(request, "registration/profile.html", page_data)

