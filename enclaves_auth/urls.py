from django.urls import path, include, re_path, reverse_lazy
from .views import *
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'enclaves_auth'
urlpatterns = [
    re_path(r'login/',  LoginUserView.as_view(), name='login'),
    re_path(r'logout/', LogoutUserView.as_view(), name='logout'),
]
