from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Post, Group, User
from django.views.generic import ListView


# Create your views here.

def index(request):
    posts: Paginator
    page_number = request.GET.get('page', 1)
    keyword = request.GET.get('q', None)
    context = {}

    if keyword:
        posts = Paginator(Post.objects.filter(text__icontains=keyword).select_related('author').select_related('group'),
                          10)
        context.update({'keyword': keyword})
    else:
        posts = Paginator(Post.objects.all(), 10)

    page_obj = posts.page(page_number)
    context.update({'posts': posts, 'page_obj': page_obj})
    return render(request, template_name='posts/index.html', context=context)


def group(request, slug):
    # slug = request.GET.get('slug')
    page = request.GET.get('page', 1)
    posts = Post.objects.filter(group__slug=slug)
    paginator = Paginator(posts, 10)
    page_obj = paginator.page(page)
    group_data = Group.objects.get(slug=slug)
    return render(request, template_name='posts/group_view.html',
                  context={'page_obj': page_obj, 'posts': posts, 'group': group_data})


class GroupsView(ListView):
    template_name = 'posts/groups_list.html'
    paginate_by = 15
    model = Group
    context_object_name = 'groups'


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    total = Post.objects.filter(author=post.author).count()
    return render(request, 'posts/detail_view.html', context={'post': post, 'total': total})