from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers



class EstudianteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudianteUser
        fields = (
            'email',
            'password',
            'estusernom',
            'estuserape',
            'estuserdocide',
            'estuserpai',
            'estuserciu',
            'estuserdir'
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True}
        }

    def create(self, validated_data):
        user = EstudianteUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            estusernom=validated_data['estusernom'],
            estuserape=validated_data['estuserape'],
            estuserdocide=validated_data['estuserdocide'],
            estuserpai=validated_data.get('estuserpai', ''),
            estuserciu=validated_data.get('estuserciu', ''),
            estuserdir=validated_data.get('estuserdir', '')
        )
        return user


class EstadoRegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoRegistro
        fields = '__all__'


class EstadoExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoExamen
        fields = '__all__'


class ProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programa
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'


class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = '__all__'


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'


class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = '__all__'


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class MatriculaProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatriculaPrograma
        fields = '__all__'


class MatriculaCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatriculaCurso
        fields = '__all__'


class RegistroCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCurso
        fields = '__all__'


class RegistroExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroExamen
        fields = '__all__'


class NotaProgramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaPrograma
        fields = '__all__'