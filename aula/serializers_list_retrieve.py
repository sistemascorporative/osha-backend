from rest_framework import serializers
from .models import *

# Define los serializers para cada modelo

class EstadoRegistroSerializerList(serializers.ModelSerializer):
    class Meta:
        model = EstadoRegistro
        fields = [
            "estregcod",
            "estregnom"
        ]


class EstudianteSerializerList(serializers.ModelSerializer):
    estestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Estudiante
        fields = [
            "estcod",
            "estnom",
            "estape",
            "estdocide",
            "estema",
            "estpai",
            "estciu",
            "estdir",
            "estestregcod"
        ]


class ProgramaSerializerList(serializers.ModelSerializer):
    proestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Programa
        fields = [
            "procod",
            "pronom",
            "proestregcod"
        ]


class CursoSerializerList(serializers.ModelSerializer):
    curprocod = ProgramaSerializerList()
    curestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Curso
        fields = [
            "curcod",
            "curnom",
            "curprocod",
            "curestregcod"
        ]


class ModuloSerializerList(serializers.ModelSerializer):
    modcurcod = CursoSerializerList()
    modestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Modulo
        fields = [
            "modcod",
            "modnom",
            "modcurcod",
            "modestregcod"
        ]


class ExamenSerializerList(serializers.ModelSerializer):
    exacurcod = CursoSerializerList()
    exaestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Examen
        fields = [
            "exacod",
            "exacurcod",
            "exaestregcod"
        ]


class PreguntaSerializerList(serializers.ModelSerializer):
    preexacod = ExamenSerializerList()
    preestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Pregunta
        fields = [
            "precod",
            "pretex",
            "preexacod",
            "preestregcod"
        ]


class AlternativaSerializerList(serializers.ModelSerializer):
    altprecod = PreguntaSerializerList()
    altestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Alternativa
        fields = [
            "altcod",
            "alttex",
            "altcor",
            "altprecod",
            "altestregcod"
        ]


class RespuestaSerializerList(serializers.ModelSerializer):
    resestcod = EstudianteSerializerList()
    resexacod = ExamenSerializerList()
    resprecod = PreguntaSerializerList()
    resaltcod = AlternativaSerializerList()
    resestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Respuesta
        fields = [
            "rescod",
            "respun",
            "resestcod",
            "resexacod",
            "resprecod",
            "resaltcod",
            "resestregcod"
        ]


class MatriculaSerializerList(serializers.ModelSerializer):
    matestcod = EstudianteSerializerList()
    matcurcod = CursoSerializerList()
    matestregcod = EstadoRegistroSerializerList()    
    class Meta:
        model = Matricula
        fields = [
            "matcod",
            "matestcod",
            "matcurcod",
            "matestregcod",
        ]


class NotaCursoSerializerList(serializers.ModelSerializer):
    notcurestcod = EstudianteSerializerList()
    notcurcurcod = CursoSerializerList()
    notcurestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = NotaCurso
        fields = [
            "notcurcod",
            "notcurpun",
            "notcurestcod",
            "notcurcurcod",
            "notcurestregcod"
        ]


class NotaProgramaSerializerList(serializers.ModelSerializer):
    notproestcod = EstudianteSerializerList()
    notproprocod = ProgramaSerializerList()
    notproestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = NotaPrograma
        fields = [
            "notprocod",
            "notpropun",
            "notproestcod",
            "notproprocod",
            "notproestregcod"
        ]