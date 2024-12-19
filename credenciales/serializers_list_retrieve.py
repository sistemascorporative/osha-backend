from rest_framework import serializers
from .models import *


# Define los serializers para cada modelo

class CredencialProgramaMatriculadoSerializerList(serializers.ModelSerializer):
    crepromatprocod = MatriculaPrograma
    class Meta:
        model = CredencialProgramaMatriculado
        fields = [
            "creprocod",
            "creprofecemi",
            "creprofeccad",
            "creprotipo",
            "creprocarnet",
            "crepromatprocod",
        ]


class CredencialProgramaSerializerList(serializers.ModelSerializer):
    creproestcod = EstudianteUser
    creproprocod = Programa
    class Meta:
        model = CredencialPrograma
        fields = [
            "creprocod",
            "creprofecemi",
            "creprofeccad",
            "creprotipo",
            "creprocarnet",
            "creproestcod",
            "creproprocod",
        ]


class CertificadoCursoMatriculadoSerializerList(serializers.ModelSerializer):
    cercurmatcurcod = MatriculaCurso
    class Meta:
        model = CertificadoCursoMatriculado
        fields = [
            "cercurcod",
            "cercurfecemi",
            "cercurfeccad",
            "cercurcarnet",
            "cercurmatcurcod",
        ]


class CertificadoCursoSerializerList(serializers.ModelSerializer):
    cercurestcod = EstudianteUser
    cercurcurcod = Curso
    class Meta:
        model = CertificadoCurso
        fields = [
            "cercurcod",
            "cercurfecemi",
            "cercurfeccad",
            "cercurcarnet",
            "cercurestcod",
            "cercurcurcod",
        ]