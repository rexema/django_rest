from .models import Project, ToDo, User
from rest_framework.serializers import ModelSerializer, Serializer, CharField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
