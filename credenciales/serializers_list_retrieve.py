from rest_framework import serializers
from .models import *
from aula.serializers_list_retrieve import *
from users.serializers_list_retrieve import EstudianteUserSerializerList, UserSimpleSerializerList


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
    creproestcod = UserSimpleSerializerList()
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
    cercurestcod = UserSimpleSerializerList()
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