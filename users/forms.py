from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=100,label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(UserCreationForm):
    pass


