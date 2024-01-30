from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm, BaseUserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from posts.models import User


class MyAuthForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Логин', 'class': 'form-control'}))
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'placeholder': 'Пароль', 'class': 'form-control'}),
    )


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
