from rest_framework.exceptions import ValidationError
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField, IntegerField, ValidationError
from .models import CustomUser


class CustomUserModelSerializer(ModelSerializer):
    email = EmailField(max_length=90)
    username = CharField(max_length=45)
    password = CharField(min_length=5, write_only=True)
    groups = StringRelatedField(many=True)

    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'password', 'groups']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        username_exists = CustomUser.objects.filter(username=attrs['username']).exists()

        if username_exists:
            raise ValidationError("User with this username exists")

        email_exists = CustomUser.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError("User with this email exists")

        return super().validate(attrs)


class UserSerializerUpdate(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['is_superuser', 'is_staff']


class UserCustomSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
