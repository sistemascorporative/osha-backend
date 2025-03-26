from djoser.serializers import UserSerializer, UserCreateSerializer
from rest_framework import serializers
from django.db import transaction
from .models import *



class CustomUserCreateSerializer(UserCreateSerializer):
    userdocide = serializers.CharField(write_only=True)
    usernom = serializers.CharField(write_only=True)
    userape = serializers.CharField(write_only=True)
    userpai = serializers.CharField(write_only=True, required=False, allow_blank=True)
    userciu = serializers.CharField(write_only=True, required=False, allow_blank=True)
    userdir = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta(UserCreateSerializer.Meta):
        model = EstudianteUser
        fields = ("email", "password", "userdocide", "usernom", "userape", "userpai", "userciu", "userdir")

    def create(self, validated_data):
        with transaction.atomic():
            userdocide = validated_data.pop("userdocide")
            usernom = validated_data.pop("usernom")
            userape = validated_data.pop("userape")
            userpai = validated_data.pop("userpai", "")
            userciu = validated_data.pop("userciu", "")
            userdir = validated_data.pop("userdir", "")

            # Buscar o crear UserSimple
            user_simple, created = UserSimple.objects.get_or_create(
                userdocide=userdocide,
                defaults={"usernom": usernom, "userape": userape, "userpai": userpai, "userciu": userciu, "userdir": userdir},
            )

            if hasattr(user_simple, "estudianteuser"):
                raise serializers.ValidationError({"error": "Este usuario ya tiene una cuenta de acceso."})

            # Crear EstudianteUser
            estudiante_user = EstudianteUser.objects.create(
                usuario=user_simple,
                email=validated_data["email"],
                is_active=False  # No activamos hasta que confirme el correo
            )
            estudiante_user.set_password(validated_data["password"])
            estudiante_user.save()

        return estudiante_user


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
        user_simple = UserSimple.objects.filter(userdocide=value).first()
        if user_simple and hasattr(user_simple, 'estudianteuser'):
            raise serializers.ValidationError("Este usuario ya tiene una cuenta de acceso.")
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