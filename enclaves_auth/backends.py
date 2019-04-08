from django.db import models
from .models import AdvUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Enter an email address')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def authenticate(self, username=None, password=None, **kwargs):
        print(username)
        try:
            user = AdvUser.objects.get(email=username)
        except AdvUser.DoesNotExist:
            return None
        except MultipleObjectsReturned:
            return AdvUser.objects.filter(email=username).order_by('id').first()

        if user.check_password(password):
            return user
        return None

    def get_user(self,user_id):
        try:
            return AdvUser.objects.get(pk=user_id)
        except AdvUser.DoesNotExist:
            return None