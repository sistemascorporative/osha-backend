from rest_framework.generics import (
    RetrieveAPIView
)
from ..serializers_list_retrieve import *
from ..serializers import *

# RetrieveAPIVIew

class EstadoRegistroRetrieveAPIView(RetrieveAPIView):
    queryset = EstadoRegistro.objects.all()
    serializer_class = EstadoRegistroSerializerList


class EstudianteRetrieveAPIView(RetrieveAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializerList


class ProgramaRetrieveAPIView(RetrieveAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializerList


class CursoRetrieveAPIView(RetrieveAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializerList


class ModuloRetrieveAPIView(RetrieveAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializerList


class ExamenRetrieveAPIView(RetrieveAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializerList


class PreguntaRetrieveAPIView(RetrieveAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializerList


class AlternativaRetrieveAPIView(RetrieveAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializerList


class RespuestaRetrieveAPIView(RetrieveAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializerList


class NotaCursoRetrieveAPIView(RetrieveAPIView):
    queryset = NotaCurso.objects.all()
    serializer_class = NotaCursoSerializerList


class NotaProgramaRetrieveAPIView(RetrieveAPIView):
    queryset = NotaPrograma.objects.all()
    serializer_class = NotaProgramaSerializerList