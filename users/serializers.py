from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import *


from rest_framework import serializers

class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    nombre = serializers.CharField(max_length=60)
    apellido = serializers.CharField(max_length=60)
    dni = serializers.CharField(max_length=50)
    pais = serializers.CharField(max_length=50, allow_blank=True, required=False)
    ciudad = serializers.CharField(max_length=50, allow_blank=True, required=False)
    direccion = serializers.CharField(max_length=100, allow_blank=True, required=False)


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