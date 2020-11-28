from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . import models



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = '__all__'
