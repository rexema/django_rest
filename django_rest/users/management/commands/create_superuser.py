from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = CustomUser.objects.filter(username='nastya').first()
        if not user:
            CustomUser.objects.create_superuser(username='nastya', email='nastya@mail.ru', password='123')
            data_user = {
                'username': 'sveta',
                'first_name': 'sveta',
                'last_name': 'sosnina',
                'email': 'sveta@mail.ru'
                }
            user = CustomUser.objects.create(**data_user)
            