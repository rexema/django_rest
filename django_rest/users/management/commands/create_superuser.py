from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        CustomUser.objects.create_superuser(username='sveta', email='sveta@mail.ru', password='sveta_2022')