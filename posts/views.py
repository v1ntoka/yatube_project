from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    return render(request, 'posts/index.html', context={'posts': posts})


def group(request, slug=None):
    text = "Здесь будет информация о группах проекта Yatube"
    return render(request, 'posts/group_list.html', context={'slug': slug, 'text': text})
