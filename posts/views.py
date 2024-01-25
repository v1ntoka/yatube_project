from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Post


# Create your views here.

def index(request):
    posts: Paginator
    page_number = request.GET.get('page')
    keyword = request.GET.get('q', None)
    if keyword:
        posts = Paginator(Post.objects.filter(text__icontains=keyword).select_related('author').select_related('group'),
                          10)
    else:
        posts = Paginator(Post.objects.all(), 10)

    try:
        page_obj = posts.page(page_number)
    except PageNotAnInteger:
        page_obj = posts.page(1)
    return render(request, template_name='posts/index.html', context={'posts': posts, 'page_obj': page_obj})
