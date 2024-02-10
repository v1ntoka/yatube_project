from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Group, User
from django.views.generic import ListView
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def index(request):
    posts: Paginator
    if request.user.is_authenticated:
        page_number = request.GET.get('page', 1)
        keyword = request.GET.get('q', None)
    else:
        page_number = 1
        keyword = None
    context = {}

    if keyword:
        posts = Paginator(Post.objects.filter(text__icontains=keyword).select_related('author').select_related('group'),
                          9)
        context.update({'keyword': keyword})
    else:
        posts = Paginator(Post.objects.all(), 9)

    page_obj = posts.page(page_number)
    context.update({'posts': posts, 'page_obj': page_obj})
    return render(request, template_name='posts/index.html', context=context)


@login_required()
def group(request, slug):
    # slug = request.GET.get('slug')
    page = request.GET.get('page', 1)
    posts = Post.objects.filter(group__slug=slug)
    paginator = Paginator(posts, 10)
    page_obj = paginator.page(page)
    group_data = Group.objects.get(slug=slug)
    return render(request, template_name='posts/group_view.html',
                  context={'page_obj': page_obj, 'posts': posts, 'group': group_data})


class GroupsView(ListView, LoginRequiredMixin):
    template_name = 'posts/groups_list.html'
    paginate_by = 15
    model = Group
    context_object_name = 'groups'


@login_required()
def post_detail(request, post_id):
    context = {}
    post = get_object_or_404(Post, pk=post_id)
    if request.user.is_staff or request.user == post.author:
        context['upd_allowed'] = True
        if request.META.get('HTTP_REFERER').find('edit') == -1:
            request.session['from'] = request.META.get('HTTP_REFERER')
    total = Post.objects.filter(author=post.author).count()
    context.update({'post': post, 'total': total})
    return render(request, 'posts/detail_view.html', context=context)


@login_required()
def post_create(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=request.user)
    return render(request, 'posts/create_view.html', context={'form': form})


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author == request.user or request.user.is_staff:
        form = PostForm(request.POST or None, files=request.FILES or None, instance=post)
        if form.is_valid():
            post.save()
            return redirect('posts:post_detail', post_id)
        context = {
            "form": form,
            "is_edit": True,
            "post": post,
        }
        return render(request, "posts/create_view.html", context)
    return redirect('posts:post_detail', post_id)


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user.is_staff or request.user == post.author:
        post.delete()
        if request.session['from']:
            return redirect(request.session['from'])
        else:
            return redirect('posts:index')
    redirect('posts:post_detail', post_id)


@login_required()
def profile(request, username):
    user = User.objects.get(username=username)
    queryset = Post.objects.filter(author__username=username)
    posts = Paginator(queryset, 10)
    page = request.GET.get('page', 1)
    page_obj = posts.get_page(page)
    total = queryset.count()
    return render(request, 'posts/profile.html', context={'page_obj': page_obj, 'user': user, 'total': total})
