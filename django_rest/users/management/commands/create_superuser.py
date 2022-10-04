from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        CustomUser.objects.create_superuser(username='nastya', email='nastya2@mail.ru', password='123')