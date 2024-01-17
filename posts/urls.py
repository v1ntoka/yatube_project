from django.urls import path
from . import views
from django.shortcuts import redirect


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    # path('contact/', views.contact, name='contact'),
    path('group/', views.GroupPostsView.as_view(), name='groups_list'),
    path("group/<slug:slug>", views.group_posts, name='group_posts'),
    path("profile/<str:username>", views.ProfileView.as_view(), name='profile'),
    # path("profile/<str:username>", views.profile_view, name='profile'),
    path("post/<int:pk>", views.PostDetailView.as_view(), name='post_detail')
]
