import io

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from todo.views import CustomUserViewSet
from .models import CustomUser
from .serializers import CustomUserModelSerializer, UserSerializerUpdate, UserCustomSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class CustomUserModelViewSet(ModelViewSet):
    serializer_class = CustomUserModelSerializer
    queryset = CustomUser.objects.all()


class CustomUserCreateView(GenericViewSet):
    serializer_class = CustomUserModelSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)


class UserListApiView(ListAPIView):
    serializer_class = UserCustomSerializer
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v1':
            return UserSerializerUpdate
        return UserCustomSerializer
