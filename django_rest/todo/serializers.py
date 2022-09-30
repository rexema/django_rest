from django.db.models import ManyToManyField
from django.forms import URLField

from .models import Project, ToDo, User
from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField, StringRelatedField


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserModelSerializer(Serializer):
    first_name = CharField(max_length=60)
    last_name = CharField(max_length=60)
    email = EmailField(default=None)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
