from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic import CreateView
from posts.models import Post, User
from .forms import MyAuthForm, CreationForm
from django.urls import reverse_lazy


class MyLogin(LoginView):
    template_name = 'users/login_view.html'
    form_class = MyAuthForm


def my_logout(request):
    logout(request)
    return render(request, 'users/logout_done_view.html')

class SignUp(CreateView):
    template_name = 'users/signup_view.html'
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')

