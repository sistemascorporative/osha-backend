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


class EstadoExamenSerializerList(serializers.ModelSerializer):
    class Meta:
        model = EstadoExamen
        fields = [
            "estexacod",
            "estexanom"
        ]


class EstudianteUserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = EstudianteUser
        fields = [
            "id",
            "email",
            "estusernom",
            "estuserape",
            "estuserdocide",
            "estuserpai",
            "estuserciu",
            "estuserdir",
        ]


class ProgramaSerializerList(serializers.ModelSerializer):
    proestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Programa
        fields = [
            "procod",
            "pronom",
            "pronumhor",
            "pronumcur",
            "procodosh",
            "proestregcod"
        ]


class CursoSerializerList(serializers.ModelSerializer):
    #curprocod = ProgramaSerializerList()
    curestregcod = EstadoRegistroSerializerList()
    class Meta:
        model = Curso
        fields = [
            "curcod",
            "curnom",
            "curnummod",
            "curfre",
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
    resestcod = EstudianteUserSerializerList()
    resexacod = ExamenSerializerList()
    resprecod = PreguntaSerializerList()
    resaltcod = AlternativaSerializerList()
    class Meta:
        model = Respuesta
        fields = [
            "rescod",
            "respun",
            "resestcod",
            "resexacod",
            "resprecod",
            "resaltcod",
            "resprocod",
        ]


class MatriculaSerializerList(serializers.ModelSerializer):
    matestcod = EstudianteUserSerializerList()
    matprocod = ProgramaSerializerList()
    matestregcod = EstadoRegistroSerializerList()    
    class Meta:
        model = Matricula
        fields = [
            "matcod",
            "matfecini",
            "matfecfin",
            "matestcod",
            "matprocod",
            "matestregcod",
        ]


class MatriculaProgramaSerializerList(serializers.ModelSerializer):
    matproprocod = ProgramaSerializerList()
    class Meta:
        model = MatriculaPrograma
        fields = [
            "matprocod",
            "matproprocod",
        ]


class MatriculaCursoSerializerList(serializers.ModelSerializer):
    matcurcurcod = CursoSerializerList()
    class Meta:
        model = MatriculaCurso
        fields = [
            "matcurcod",
            "matcurcurcod",
        ]


class RegistroExamenSerializerList(serializers.ModelSerializer):
    regexaestexacod = EstadoExamenSerializerList()
    regexaestcod = EstudianteUserSerializerList()
    regexaexacod = ExamenSerializerList()
    class Meta:
        model = RegistroExamen
        fields = [
            "regexacod",
            "regexapun",
            "regexaint",
            "regexaestexacod",
            "regexaestcod",
            "regexaexacod"
        ]


class RegistroExamenProgramaSerializerList(serializers.ModelSerializer):
    regexaproestexacod = EstadoExamenSerializerList()
    regexapromatprocod = MatriculaProgramaSerializerList()
    regexaproexacod = ExamenSerializerList()
    class Meta:
        model = RegistroExamenPrograma
        fields = [
            "regexaprocod",
            "regexapropun",
            "regexaproint",
            "regexaproestexacod",
            "regexapromatprocod",
            "regexaproexacod"
        ]


class RegistroExamenCursoSerializerList(serializers.ModelSerializer):
    regexacurestexacod = EstadoExamenSerializerList()
    regexacurmatcurcod = MatriculaCursoSerializerList()
    regexacurexacod = ExamenSerializerList()
    class Meta:
        model = RegistroExamenCurso
        fields = [
            "regexacurcod",
            "regexacurpun",
            "regexacurint",
            "regexacurestexacod",
            "regexacurmatcurcod",
            "regexacurexacod"
        ]


class NotaProgramaSerializerList(serializers.ModelSerializer):
    notproestcod = EstudianteUserSerializerList()
    notproprocod = ProgramaSerializerList()
    class Meta:
        model = NotaPrograma
        fields = [
            "notprocod",
            "notpropun",
            "notproestcod",
            "notproprocod"
        ]

class XAlternativaSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Alternativa
        fields = [
            "altcod",
            "alttex",
            "altcor",
            "altprecod",
            "altestregcod"
        ]


class XPreguntaSerializerList(serializers.ModelSerializer):
    alternativas = XAlternativaSerializerList(many=True, source='alternativa_set')
    
    class Meta:
        model = Pregunta
        fields = [
            "precod",
            "pretex",
            "preexacod",
            "preestregcod",
            "alternativas"
        ]


class XExamenSerializerList(serializers.ModelSerializer):
    preguntas = XPreguntaSerializerList(many=True, source='pregunta_set')
    exacurcod = CursoSerializerList()
    exaestregcod = EstadoRegistroSerializerList()
    
    class Meta:
        model = Examen
        fields = [
            "exacurcod",
            "exaestregcod",
            "preguntas"
        ]