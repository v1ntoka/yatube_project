from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordChangeDoneView, PasswordResetConfirmView


app_name = 'users'

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='users/login_view.html'), name='login'),
    path('auth/login/', views.MyLogin.as_view(), name='login'),
    path('auth/logout/', views.my_logout, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('register/', views.SignUp.as_view(), name='signup'),
    # path(
    #     "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    # ),
    # path(
    #     "password_change/done/",
    #     views.PasswordChangeDoneView.as_view(),
    #     name="password_change_done",
    # ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),

]
