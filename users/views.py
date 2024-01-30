from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from posts.models import Post, User
from .forms import MyAuthForm, CreationForm
from django.urls import reverse_lazy


class MyLogin(LoginView):
    template_name = 'users/login_view.html'
    form_class = MyAuthForm


def my_logout(request):
    logout(request)
    return render(request, 'users/logout_view.html')


def profile(request, username):
    user = User.objects.get(username=username)
    queryset = Post.objects.filter(author__username=username)
    posts = Paginator(queryset, 10)
    page = request.GET.get('page', 1)
    page_obj = posts.get_page(page)
    total = queryset.count()
    return render(request, 'users/profile.html', context={'page_obj': page_obj, 'user': user, 'total': total})


class SignUp(CreateView):
    form_class = CreationForm
    template_name = "users/signup_view.html"
    success_url = reverse_lazy('users:login')
