from django.urls import include, path
from django.shortcuts import reverse, redirect
from . import views

app_name = 'about'

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('tech/', views.TechView.as_view(), name='tech'),
    # path('', lambda request: redirect('contact/')),
    path('', views.AboutView.as_view(), name='about'),
]
