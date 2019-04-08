from django.db import models
from django.contrib.auth.models import AbstractUser

# кастомный юзверь
class AdvUser(AbstractUser):
    username = models.CharField(blank=True, max_length=50, unique=False)
    email = models.EmailField(verbose_name='email', unique=True, blank=False) # changes email to unique and blank to false
    send_messages = models.BooleanField(default=True, verbose_name='Слать рассылку по игре?')
    is_activeted  = models.BooleanField(default=True, verbose_name='Прошел ли активацию?', db_index=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS

    class Meta(AbstractUser.Meta):
        pass
