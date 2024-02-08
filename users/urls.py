from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'users'

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='users/login_view.html'), name='login'),
    path('login/', views.MyLogin.as_view(), name='login'),
    path('logout/', views.my_logout, name='logout'),
    path('register/', views.SignUp.as_view(), name='signup'),
    path(
        "password_change/", PasswordChangeView.as_view(template_name='users/password_change_form.html'),
        name="password_change"
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name="password_change_done",
    ),
    path("password_reset/", PasswordResetView.as_view(template_name='users/password_reset_view.html'),
         name="password_reset"),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name='users/password_reset_done_view.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm_view.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(template_name='users/password_reset_complete_view.html'),
        name="password_reset_complete",
    ),

]
