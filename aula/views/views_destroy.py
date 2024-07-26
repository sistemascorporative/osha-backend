from rest_framework.generics import (
    RetrieveDestroyAPIView
)
from ..serializers import *


class EstadoRegistroDestroyAPIView(RetrieveDestroyAPIView):
    queryset = EstadoRegistro.objects.all()
    serializer_class = EstadoRegistroSerializer


class EstudianteUserDestroyAPIView(RetrieveDestroyAPIView):
    queryset = EstudianteUser.objects.all()
    serializer_class = EstudianteUserSerializer


class ProgramaDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class CursoDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ModuloDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class ExamenDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer


class PreguntaDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class AlternativaDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer


class RespuestaDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


class MatriculaDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class RegistroCursoDestroyAPIView(RetrieveDestroyAPIView):
    queryset = RegistroCurso.objects.all()
    serializer_class = RegistroCursoSerializer


class NotaProgramaDestroyAPIView(RetrieveDestroyAPIView):
    queryset = NotaPrograma.objects.all()
    serializer_class = NotaProgramaSerializer