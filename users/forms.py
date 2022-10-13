"""
A quick note here. We have created both UserUpdateForm and ProfileUpdateForm where former has username and email and the latter has image. 
You might be wondering how it will be possible to update username and email since ProfileUpdateForm is missing those. Well, first, because we have
signals defined in signals.py. Thus, everytime a User instance is created a Profile is created too, and, if a User instance is updated, the 
profile also gets updated. Also, secondly, once we put them in a template, UserUpdateForm and ProfileUpdateForm will be making more sense. See the 
html form in profile.html
"""



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User # model = User since whenever validated, we want to create a new user
        fields = ("username", "email", "password1", "password2")

class UserUpdateForm(forms.ModelForm): # UserUpdateForm for when user wants to update username or email
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")

class ProfileUpdateForm(forms.ModelForm): # ProfileUpdateForm for when user wants to update username or email
    class Meta:
        model = Profile # since this is our ProfileUpdateForm we're not equating our model variable to User (as was the case above with UserUpdateForm) but rather Profile from models
        fields = ['image'] # since we can already update username and email with UserUpdateForm, we don't need to write them again. 