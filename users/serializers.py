from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializer(UserSerializer):
    class Meta:
        model = EstudianteUser
        fields = ('usuario', 'email', 'password')


class EstudianteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudianteUser
        fields = '__all__'


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSimple
        fields = '__all__'