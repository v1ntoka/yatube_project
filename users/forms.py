from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms.widgets import PasswordInput, TextInput


class MyAuthForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'placeholder': 'Password', 'class': 'form-control'}),
    )
