from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()



class UserCreateSerializar(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('email', 'password')


class EstudianteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudianteUser
        fields = '__all__'


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSimple
        fields = '__all__'