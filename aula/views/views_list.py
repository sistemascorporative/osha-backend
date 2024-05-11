from rest_framework.generics import (
    ListAPIView
)
from ..serializers_list_retrieve import *
from ..serializers import *
from rest_framework import permissions

#ListAPIViews

class EstadoRegistroListAPIView(ListAPIView):
    queryset = EstadoRegistro.objects.all()
    serializer_class = EstadoRegistroSerializerList


class EstudianteListAPIView(ListAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializerList


class ProgramaListAPIView(ListAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializerList


class CursoListAPIView(ListAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializerList


class ModuloListAPIView(ListAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializerList


class ExamenListAPIView(ListAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializerList


class PreguntaListAPIView(ListAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializerList


class AlternativaListAPIView(ListAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializerList


class RespuestaListAPIView(ListAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializerList


class MatriculaListAPIView(ListAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializerList


class RegistroCursoListAPIView(ListAPIView):
    queryset = RegistroCurso.objects.all()
    serializer_class = RegistroCursoSerializerList


class NotaProgramaListAPIView(ListAPIView):
    queryset = NotaPrograma.objects.all()
    serializer_class = NotaProgramaSerializerList