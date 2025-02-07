from rest_framework.generics import (
    RetrieveDestroyAPIView
)
from ..serializers import *


class EstadoRegistroDestroyAPIView(RetrieveDestroyAPIView):
    queryset = EstadoRegistro.objects.all()
    serializer_class = EstadoRegistroSerializer


class EstadoExamenDestroyAPIView(RetrieveDestroyAPIView):
    queryset = EstadoExamen.objects.all()
    serializer_class = EstadoExamenSerializer


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



