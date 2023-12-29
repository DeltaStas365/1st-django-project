from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError("Password doesn't match")
        return cd['confirm_password']

class ProfileForm(forms.Form):
    username = forms.CharField(label="username", widget=forms.TextInput)
    email = forms.EmailField(label="email", widget=forms.TextInput)


class ChangePassword(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput)
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput)

    def clean_old_password(self):
        password = self.cleaned_data["old_password"]
        if not self.user.check_password(password):
            self.add_error("old_password", forms.ValidationError("Incorrect password!"))
        return password

    def clean_new_password_repeat(self):
        password1 = self.cleaned_data["new_password"]
        password2 = self.cleaned_data["confirm_new_password"]
        if password1 != password2:
            self.add_error("confirm_new_password", forms.ValidationError("Password doesn't match!"))
        return password1