from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group, name='groups_list'),
    path("group/<slug:slug>", views.group, name='group_detail')
]
