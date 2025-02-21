from rest_framework import serializers
from .models import *
from aula.serializers_list_retrieve import *


# Define los serializers para cada modelo

class CredencialProgramaMatriculadoSerializerList(serializers.ModelSerializer):
    crepromatprocod = MatriculaProgramaSerializerList()
    class Meta:
        model = CredencialProgramaMatriculado
        fields = [
            "creprocod",
            "creprofecemi",
            "creprofeccad",
            "creprocer",
            "creprodip",
            "creprocarnet",
            "crepromatprocod",
        ]


class CredencialProgramaSerializerList(serializers.ModelSerializer):
    #creproestcod = EstudianteUserSerializerList()
    creproprocod = ProgramaSerializerList()
    class Meta:
        model = CredencialPrograma
        fields = [
            "creprocod",
            "creprofecemi",
            "creprofeccad",
            "creprocer",
            "creprodip",
            "creprocarnet",
            "creproestcod",
            "creproprocod",
        ]


class CertificadoCursoMatriculadoSerializerList(serializers.ModelSerializer):
    cercurmatcurcod = MatriculaCursoSerializerList()
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
    #cercurestcod = EstudianteUserSerializerList()
    cercurcurcod = CursoSerializerList()
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