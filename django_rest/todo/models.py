from django.db import models
from users.models import CustomUser

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    name = models.CharField(max_length=80)
    link = models.URLField(default=None)
    users = models.ManyToManyField(CustomUser)

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    text = models.TextField(max_length=120)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    is_accomplished = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
