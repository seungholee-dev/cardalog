from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django_countries.fields import CountryField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', "Male"), ('F', 'Female')])
    country = CountryField().formfield()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', 'gender', 'country']