from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # + country
    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2']