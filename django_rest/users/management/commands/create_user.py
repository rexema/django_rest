from django.core.management.base import BaseCommand
from users.models import CustomUser
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('total', type=int)

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            CustomUser.objects.create_user(username=get_random_string(7), first_name=get_random_string(7),
                                           last_name=get_random_string(10), email=get_random_string(5))