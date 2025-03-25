from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import *



class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    usernom = serializers.CharField(max_length=60)
    userape = serializers.CharField(max_length=60)
    userdocide = serializers.CharField(max_length=50)
    userpai = serializers.CharField(max_length=50, allow_blank=True, required=False)
    userciu = serializers.CharField(max_length=50, allow_blank=True, required=False)
    userdir = serializers.CharField(max_length=100, allow_blank=True, required=False)
    
    def validate_email(self, value):
        if EstudianteUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está registrado.")
        return value

    def validate_userdocide(self, value):
        if UserSimple.objects.filter(userdocide=value).exists():
            raise serializers.ValidationError("Este documento de identidad ya está registrado.")
        return value


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