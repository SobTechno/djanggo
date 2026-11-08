from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=100,label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput())


