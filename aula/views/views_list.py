from rest_framework.generics import (
    ListAPIView
)
from ..serializers_list_retrieve import *
from ..serializers import *
from ..models import Curso, Programa
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


#ListAPIViews


# Devuelve todos los programas por X estudiante matriculado
class ProgramasPorEstudianteListAPIView(ListAPIView):
    serializer_class = ProgramaSerializer
    
    def get_queryset(self):
        estudiante_id = self.kwargs.get('estudiante_id')
        if estudiante_id is not None:
            try:
                estudiante = EstudianteUser.objects.get(pk=estudiante_id)
                matriculas = Matricula.objects.filter(matestcod=estudiante)
                programas = [matricula.matprocod for matricula in matriculas]
                return programas
            except EstudianteUser.DoesNotExist:
                return Programa.objects.none()
        else:
            return Programa.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"detail": "Estudiante not found or no programs enrolled."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Devuelve todos los cursos por X programa
class CursosPorProgramaListAPIView(ListAPIView):
    serializer_class = CursoSerializer

    def get_queryset(self):
        procod = self.kwargs.get('programa_id')
        if procod is not None:
            try:
                programa = Programa.objects.get(procod=procod)
                return programa.cursos.all()
            except Programa.DoesNotExist:
                return Curso.objects.none()
        else:
            return Curso.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"detail": "Programa not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Devuelve todos los módulos por X curso
class ModulosPorCursoListAPIView(ListAPIView):
    serializer_class = ModuloSerializer

    def get_queryset(self):
        curcod = self.kwargs.get('curso_id')        
        if curcod is not None:
            try:
                modulo = Modulo.objects.filter(modcurcod__curcod=curcod)
                print(modulo)
                return modulo
            except Modulo.DoesNotExist:
                return Modulo.objects.none()
        else:       
            return Modulo.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"detail": "Modulos not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class EstudianteUserListAPIView(ListAPIView):
    queryset = EstudianteUser.objects.all()
    serializer_class = EstudianteUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset()


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