from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    name = models.CharField(max_length=80)
    link = models.URLField(default=None)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    text = models.TextField(max_length=120)
    date_of_creation = models.DateField()
    date_of_update = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    is_accomplished = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
