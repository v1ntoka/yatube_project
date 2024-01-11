from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from .views import my_logout, SignUp
app_name = 'users'

# class MyLogout(LogoutView):
#     template_name = "users/logged_out.html"
#     http_method_names = LogoutView.http_method_names + ["get"]


urlpatterns = [
    # path('logout/', MyLogout.as_view(), name='logout')
    path('logout/', my_logout, name='logout'),
    path('signup/', SignUp.as_view(), name='signup')
]
