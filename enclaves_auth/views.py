from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

"""
Отдельный модуль для авторизации, аутентификации, регистрации пользователей
"""

# логин
class LoginUserView(LoginView):
    template_name = 'enclaves_auth/login.html'
    def get_success_url(self):
        return reverse("enclaves_main:index")
        #url = self.get_redirect_url()
        #if url:
        #    return url
        #elif self.request.user.is_superuser:
        #    return reverse("admin")
        #else:
        #    return reverse("enclaves_main:index")

# логаут
class LogoutUserView(LogoutView):
    next_page='/'

# регистрация

# активация

# смена пароля
