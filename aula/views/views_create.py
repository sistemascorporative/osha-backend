from rest_framework.generics import (
    CreateAPIView
)
from ..serializers import *
from rest_framework import authentication


class EstadoRegistroCreateAPIView(CreateAPIView):
    queryset = EstadoRegistro.objects.all()
    serializer_class = EstadoRegistroSerializer


class EstudianteCreateAPIView(CreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class ProgramaCreateAPIView(CreateAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class CursoCreateAPIView(CreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ModuloCreateAPIView(CreateAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class ExamenCreateAPIView(CreateAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer


class PreguntaCreateAPIView(CreateAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class AlternativaCreateAPIView(CreateAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer


class RespuestaCreateAPIView(CreateAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


class MatriculaCreateAPIView(CreateAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class NotaCursoCreateAPIView(CreateAPIView):
    queryset = NotaCurso.objects.all()
    serializer_class = NotaCursoSerializer


class NotaProgramaCreateAPIView(CreateAPIView):
    queryset = NotaPrograma.objects.all()
    serializer_class = NotaProgramaSerializer