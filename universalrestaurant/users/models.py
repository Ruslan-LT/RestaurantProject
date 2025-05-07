from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='users/images', blank=True, null=True, verbose_name='Аватар')

    class Meta:
        db_table = 'User'
        verbose_name = 'Користувача'
        verbose_name_plural = 'Користувачі'


    def __str__(self):
        return self.username

