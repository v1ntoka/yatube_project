from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import CreateView
from .forms import CreationForm
from django.urls import reverse_lazy


def my_logout(request):
    logout(request)
    return render(request, 'users/logged_out.html')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'
