from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models import fields
from django_countries.fields import CountryField


# User registration form with some custom fields
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[(True, "Male"), (False, 'Female')])
    country = CountryField().formfield()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', 'gender', 'country']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['image', 'username', 'email']