from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
from django.core.paginator import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView


# @login_required(login_url='users:login')
def index(request):
    # post_list = Paginator(Post.objects.all().order_by('-pub_date'), 10)
    page_number = request.GET.get('page')
    keyword = request.GET.get('q', None)
    if keyword:
        posts = Paginator(
            Post.objects.filter(text__icontains=keyword).select_related('author').select_related('group').order_by(
                '-pub_date'), 10)
    else:
        posts = Paginator(Post.objects.all().order_by('-pub_date'), 10)
    try:
        page_obj = posts.page(page_number)
    except PageNotAnInteger:
        page_obj = posts.page(1)
    return render(request, 'posts/index.html', context={'posts': posts, 'page_obj': page_obj})


@login_required(login_url='users:login')
def group(request, slug=None):
    text = "Здесь будет информация о группах проекта Yatube"
    return render(request, 'posts/group_list.html', context={'slug': slug, 'text': text})


@login_required(login_url='users:login')
def group_posts(request, slug):
    groups = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=groups).order_by('-pub_date')[:10]
    context = {'group': groups, 'posts': posts}
    return render(request, 'posts/group_list.html', context=context)


class GroupPostsView(LoginRequiredMixin, TemplateView):
    template_name = 'posts/groups.html'
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


# @login_required(login_url='/users/login')
# def profile_view(request, username):
#     profile = get_object_or_404(User, username=username)
#     posts = Post.objects.filter(author=profile).order_by('-pub_date')
#     context = {'profile': profile, 'posts': posts}
#     return render(request, 'posts/profile.html', context)

class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'posts/profile.html'
    login_url = 'users:login'
    redirect_field_name = 'redirect_to'
    paginate_by = 5
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=get_object_or_404(User, username=self.kwargs['username'])).order_by(
            '-pub_date')

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = get_object_or_404(User, username=self.kwargs['username'])
        context['total_posts'] = self.get_queryset().count()
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = 'users:login'
    template_name = 'posts/detail_view.html'
    redirect_field_name = 'redirect_to'
    context_object_name = 'posts'
    model = Post

    # def get_queryset(self):
    #     # return Post.objects.get(id=self.kwargs['pk'])
    #     return get_object_or_404(Post, id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        context['total_posts'] = Post.objects.filter(author=context['post'].author).count()
        return context
