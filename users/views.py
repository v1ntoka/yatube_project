from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView
from posts.models import Post, User
from .forms import MyAuthForm, CreationForm
from django.urls import reverse_lazy


class MyLogin(LoginView):
    template_name = 'users/login_view.html'
    form_class = MyAuthForm


def my_logout(request):
    logout(request)
    context = {'what': "Вы вышли из своей учётной записи. Ждём вас снова!", "header": "Выход", "title": "Вы вышли из системы"}
    return render(request, 'users/done.html', context=context)


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
    template_name = "users/user_form_multitask.html"
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['what'] = 'Зарегистрироваться'
        return context


class MyPasswordChangeView(PasswordChangeView):
    template_name = "users/user_form_multitask.html"
    success_url = reverse_lazy('users:password_change_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['what'] = 'Изменить пароль'
        return context


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "users/done.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['what'] = "Пароль успешно изменен"
        context['header'] = "Изменение пароля"
        context['title'] = context['header']
        return context