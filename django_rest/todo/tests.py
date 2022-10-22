import json

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase

from mixer.backend.django import mixer
from users.models import CustomUser
from .views import CustomUserViewSet, ProjectViewSet
from .models import Project, ToDo


class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.url = '/api/project/'
        self.projects = {'name': 'Django', 'link': 'https://timeweb.com/'}
        self.projects_fake = {'name': 'Django2', 'link': 'https://timeweb2.com/'}
        self.format = 'json'
        self.login = 'admin@mail.ru'
        self.password = 'admin_1123'
        self.admin = CustomUser.objects.create_superuser(self.login, self.password)
        self.project = Project.objects.create(**self.projects)

    # Тестирование с помощью класса APIRequestFactory

    def test_factory_client_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url, format=self.format)
        view = CustomUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тестирование с помощью класса APIClient

    def test_api_update_guest(self):
        client = APIClient()
        response = client.put(f'{self.url}{self.project.id}/', **self.projects_fake)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def tearDown(self) -> None:
        pass


class TestTodo(APITestCase):
    def setUp(self) -> None:
        self.url = '/api/todo/'
        self.url2 = '/api/project/'
        self.projects = {'name': 'Django', 'link': 'https://timeweb.com/'}
        self.projects_fake = {'name': 'Django2', 'link': 'https://timeweb2.com/'}
        self.format = 'json'
        self.login = 'admin@mail.ru'
        self.password = 'admin_1123'
        self.admin = CustomUser.objects.create_superuser(self.login, self.password)
        self.project = Project.objects.create(**self.projects)

    def test_api_test_case_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_test_case_update_admin(self):
        user_test = CustomUser.objects.create_superuser('admin3425@mail.ru', '12356436w')
        self.client.login(username='admin3425@mail.ru', password='12356436w')
        response = self.client.put(f'{self.url2}{self.project.id}/', self.projects_fake)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.project.refresh_from_db()
        self.assertEqual(self.project.name, self.projects_fake.get('name'))
        self.assertEqual(self.project.link, self.projects_fake.get('link'))
        self.client.logout()

    def test_mixer(self):
        proj = mixer.blend(Project, link='mail.ru')
        self.client.force_login(user=self.admin)
        # response = self.client.get(self.url2)
        response = self.client.get(f'{self.url2}{proj.id}/', self.projects_fake)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(proj.link, 'mail.ru')

    def tearDown(self) -> None:
        pass
