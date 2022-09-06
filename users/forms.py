from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User # model = User since whenever validated, we want to create a new user
        fields = ("username", "email", "password1", "password2")