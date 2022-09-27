from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField, IntegerField
from .models import CustomUser


class CustomUserSerializer(Serializer):
    username = CharField(max_length=64)
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64)
    email = EmailField(max_length=254)

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.save()
        return user

    def validate_email(self, value):
        if value == IntegerField:
            raise ValidationError('email should be string')
        return value

    def validate(self, attrs):
        if attrs.get('last_name') == 'Sosnina' and attrs.get('first_name') != 'Anastasia':
            raise ValidationError('my name must be Anastasia')
        return attrs

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class CustomUserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email']
