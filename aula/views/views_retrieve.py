from rest_framework.generics import (
    RetrieveAPIView
)
from ..serializers_list_retrieve import *
from ..serializer import *

# RetrieveAPIVIew

class EStadoRegistroRetrieveAPIVIew(RetrieveAPIView):
    queryset = EstadoRegistro.objects.all()
    serializer_class = EstadoRegistroSerializerList


class EstudianteRetrieveAPIVIew(RetrieveAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializerList


class ProgramaRetrieveAPIVIew(RetrieveAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializerList


class CursoRetrieveAPIVIew(RetrieveAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializerList


class ModuloRetrieveAPIVIew(RetrieveAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializerList


class ExamenRetrieveAPIVIew(RetrieveAPIView):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializerList


class PreguntaRetrieveAPIVIew(RetrieveAPIView):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializerList


class AlternativaRetrieveAPIVIew(RetrieveAPIView):
    queryset = Alternativa.objects.all()
    serializer_class = AlternativaSerializerList


class RespuestaRetrieveAPIVIew(RetrieveAPIView):
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializerList


class NotaCursoRetrieveAPIVIew(RetrieveAPIView):
    queryset = NotaCurso.objects.all()
    serializer_class = NotaCursoSerializerList


class NotaProgramaRetrieveAPIVIew(RetrieveAPIView):
    queryset = NotaPrograma.objects.all()
    serializer_class = NotaProgramaSerializerList