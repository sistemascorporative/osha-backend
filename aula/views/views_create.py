from rest_framework.generics import (
    CreateAPIView
)
from ..serializers import *
from ..models import *


class EstadoRegistroCreateAPIView(CreateAPIView):
    queryset = EstadoRegistro.objects.all()
    serializer_class = EstadoRegistroSerializer


class EstadoExamenCreateAPIView(CreateAPIView):
    queryset = EstadoExamen.objects.all()
    serializer_class = EstadoExamenSerializer


class EstudianteUserCreateAPIView(CreateAPIView):
    queryset = EstudianteUser.objects.all()
    serializer_class = EstudianteUserSerializer


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


class RegistroExamenCreateAPIView(CreateAPIView):
    queryset = RegistroExamen.objects.all()
    serializer_class = RegistroExamenSerializer


class RegistroCursoCreateAPIView(CreateAPIView):
    queryset = RegistroCurso.objects.all()
    serializer_class = RegistroCursoSerializer


class NotaProgramaCreateAPIView(CreateAPIView):
    queryset = NotaPrograma.objects.all()
    serializer_class = NotaProgramaSerializer