from django.shortcuts import render

from users.forms import UserRegistrationForm


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
    return render(request, "registration/profile.html")
