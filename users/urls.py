from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordChangeDoneView, PasswordResetConfirmView
from django.urls import path
from .views import my_logout, SignUp

app_name = 'users'

# class MyLogout(LogoutView):
#     template_name = "users/logged_out.html"
#     http_method_names = LogoutView.http_method_names + ["get"]


urlpatterns = [
    # path('logout/', MyLogout.as_view(), name='logout')
    path('logout/', my_logout, name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/change_password.html'),
         name='change_password'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html')),
    path('password_reset/', PasswordResetView.as_view(template_name='users/reset_password.html'),
         name='password_reset_form'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html')),
    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetDoneView.as_view(template_name='users/password_change_done.html')),
]
