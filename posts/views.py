from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    return render(request, 'posts/index.html', context={'posts': posts})


def group(request, slug=None):
    text = "Здесь будет информация о группах проекта Yatube"
    return render(request, 'posts/group_list.html', context={'slug': slug, 'text': text})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {'group': group, 'posts': posts}
    return render(request, 'posts/group_list.html', context=context)
