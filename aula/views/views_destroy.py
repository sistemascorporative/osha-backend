from rest_framework.generics import (
    RetrieveDestroyAPIView
)
from ..serializers import *


class EstadoRegistroDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = EstadoRegistro.objects,all()
    serializer_class = EstadoRegistroSerializer


class EstudianteDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer


class ProgramaDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer


class CursoDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class ModuloDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer


class ExamenDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer


class PreguntaDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class AlternativaDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializer


class RespuestaDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer


class NotaCursoDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = NotaCurso.objects.all()
    serializer_class = NotaCursoSerializer


class NotaProgramaDestroyAPIVIew(RetrieveDestroyAPIView):
    queryset = NotaPrograma.objects.all()
    serializer_class = NotaProgramaSerializer