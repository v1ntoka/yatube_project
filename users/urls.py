from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordChangeDoneView, PasswordResetConfirmView


app_name = 'users'

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='users/login_view.html'), name='login'),
    path('auth/login/', views.MyLogin.as_view(), name='login'),
    path('auth/logout/', views.my_logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile')

]
