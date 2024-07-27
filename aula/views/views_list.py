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
        estudiante_email = self.kwargs.get('estudiante_email')
        if estudiante_email is not None:
            try:
                estudiante = EstudianteUser.objects.get(email=estudiante_email)
                matriculas = Matricula.objects.filter(matestcod=estudiante)
                if not matriculas:
                    raise Matricula.DoesNotExist("Usted aún no se matriculado a ningún programa")
                programas = [matricula.matprocod for matricula in matriculas]
                return programas
            except EstudianteUser.DoesNotExist:
                raise EstudianteUser.DoesNotExist("Estudiante no encontrado.")
            except Matricula.DoesNotExist:
                raise Matricula.DoesNotExist("Usted aún no se matriculado a ningún programa.")
        else:
            return Programa.objects.none()

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            if not queryset:
                return Response({"detail": "Estudiante  no encontrado o no hay programas inscritos."}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except EstudianteUser.DoesNotExist as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Matricula.DoesNotExist as e:
            return Response({"detail": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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



# Devuelve todos los registros de examenes de X programa
class RegistrosExamenesPorProgramaListAPIView(ListAPIView):
    serializer_class = RegistroExamenSerializer
    
    def get_queryset(self):
        programa_id = self.kwargs.get('programa_id')
        if programa_id is not None:
            try:
                programa = Programa.objects.get(procod=programa_id)
                cursos = programa.cursos.all()
                # Obtener los exámenes asociados a los cursos del programa
                examenes = Examen.objects.filter(exacurcod__in=cursos)
                # Obtener los registros de examen asociados a los exámenes
                registros_examen = RegistroExamen.objects.filter(regexaexacod__in=examenes)
                return registros_examen
            except Programa.DoesNotExist:
                return RegistroExamen.objects.none()
        else:
            return RegistroExamen.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"detail": "No se encontraron registros de exámenes para este programa."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Devuelve todos los examenes de X programa
class ExamenesPorProgramaListAPIView(ListAPIView):
    serializer_class = ExamenSerializer
    
    def get_queryset(self):
        programa_id = self.kwargs.get('programa_id')
        if programa_id is not None:
            try:
                programa = Programa.objects.get(procod=programa_id)
                cursos = programa.cursos.all()
                examenes = Examen.objects.filter(exacurcod__in=cursos)
                return examenes
            except Programa.DoesNotExist:
                return Examen.objects.none()
        else:
            return Examen.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset:
            return Response({"detail": "No se encontraron exámenes para este programa."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Estudiante
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
    queryset = EstudianteUser.objects.all()
    serializer_class = EstudianteUserSerializerList


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