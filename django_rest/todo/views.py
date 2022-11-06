import io

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view, renderer_classes, action
from users.serializers import CustomUserModelSerializer
from .filters import UserFilter, ProjectFilter, ToDoFilter
from .models import Project, ToDo, User
from .serializers import ProjectSerializer, ToDoSerializer, UserSerializer, UserModelSerializer
from django_filters import rest_framework as filters
from users.models import CustomUser
from rest_framework import filters


class UserPagination(PageNumberPagination):
    page_size = 2


class ToDoPagination(PageNumberPagination):
    page_size = 20


class UserModelViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('id')
    filterset_class = UserFilter
    # pagination_class = UserPagination


class CustomUserViewSet(ModelViewSet):
    serializer_class = CustomUserModelSerializer
    queryset = CustomUser.objects.all()


class UserViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()

    def list(self, request):
        user = User.objects.all()
        serializer_class = UserSerializer(user, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer_class = UserSerializer(user)
        return Response(serializer_class.data)


class ProjectViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().order_by('id')
    # pagination_class = UserPagination
    filterset_class = ProjectFilter


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class ToDoViewSet(ModelViewSet):
    # permission_classes = [AdminOnly]
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all().order_by('id')
    filterset_class = ToDoFilter

    # pagination_class = ToDoPagination

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_deleted = True
        todo.save()
        return HttpResponse('deleted')


def user_get(request):
    user = User.objects.get(pk=2)
    serializer = UserModelSerializer(user)

    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


@csrf_exempt
def user_post(request, pk=None):
    json_data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = UserModelSerializer(data=json_data)
    elif request.method == 'PUT':
        user = User.objects.get(pk=pk)
        serializer = UserModelSerializer(user, data=json_data)
    elif request.method == 'PATCH':
        user = User.objects.get(pk=pk)
        serializer = UserModelSerializer(user, data=json_data, partial=True)

    if serializer.is_valid():
        user = serializer.save()

        serializer = UserModelSerializer(user)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)

    return HttpResponseBadRequest(JSONRenderer().render(serializer.errors))
