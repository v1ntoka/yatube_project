from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>', views.group, name='group'),
    path('groups/', views.GroupsView.as_view(), name='groups'),
    path('post/<int:pk>', views.post_detail, name='post_detail')
]