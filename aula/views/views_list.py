from rest_framework.generics import (
    ListAPIView
)
from ..serializers_list_retrieve import *
from ..serializers import *
from ..models import Curso, Programa
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


#ListAPIViews


# Devuelve todos los programas matriculados de X estudiante
class ProgramasMatriculadosPorEstudianteListAPIView(ListAPIView):
    serializer_class = ProgramaSerializer
    
    def get_queryset(self):
        estudiante_email = self.kwargs.get('estudiante_email')
        if not estudiante_email:
            return Programa.objects.none()
        # Filtrar programas directamente mediante la relación en MatriculaPrograma
        return Programa.objects.filter(matriculaprograma__matproestcod__email=estudiante_email)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Manejar el caso en el que no se encuentra el email del estudiante
        if not queryset.exists() and not EstudianteUser.objects.filter(email=self.kwargs.get('estudiante_email')).exists():
            return Response(
                {"detail": "El estudiante con el email proporcionado no existe."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Devuelve todos los cursos matriculados de X estudiante
class CursosMatriculadosPorEstudianteListAPIView(ListAPIView):
    serializer_class = CursoSerializerList

    def get_queryset(self):
        estudiante_email = self.kwargs['estudiante_email']
        return Curso.objects.filter(matriculacurso__matcurestcod__email=estudiante_email)


# Devuelve todos los cursos gratuitos
class CursosGratuitosListAPIView(ListAPIView):
    queryset = Curso.objects.filter(curfre=True)
    serializer_class = CursoSerializerList



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



"""
Endpoint para obtener las matrículas de programas según el correo del estudiante.
"""
class MatriculaProgramaPorEstudianteListView(ListAPIView):
    serializer_class = MatriculaProgramaSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        return MatriculaPrograma.objects.filter(matproestcod=estudiante)


"""
Endpoint para obtener los registros de exámenes de programa.
"""
class RegistroExamenProgramaPorMatriculaListView(ListAPIView):
    serializer_class = RegistroExamenProgramaSerializerList

    def get_queryset(self):
        matprocod = self.kwargs.get('codigo_matricula')        
        return RegistroExamenPrograma.objects.filter(regexapromatprocod=matprocod)


"""
Endpoint para obtener las matrículas de cursos según el correo del estudiante.
"""
class MatriculaCursoPorEstudianteListView(ListAPIView):
    serializer_class = MatriculaCursoSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        return MatriculaCurso.objects.filter(matcurestcod=estudiante)


"""
Endpoint para obtener todos los registros de exámenes de cursos de un estudiante.
"""
class RegistroExamenCursoPorEstudianteListView(ListAPIView):
    serializer_class = RegistroExamenCursoSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        matriculas_curso = MatriculaCurso.objects.filter(matcurestcod=estudiante)
        return RegistroExamenCurso.objects.filter(regexacurmatcurcod__in=matriculas_curso)



# Devuelve todos los registros de examenes de X programa y X estudiante
class RegistrosExamenesPorProgramaPorEstudianteListAPIView(ListAPIView):
    serializer_class = RegistroExamenProgramaSerializerList
    
    def get_queryset(self):
        programa_id = self.kwargs.get('programa_id')
        estudiante_id = self.kwargs.get('estudiante_id')
        print(f"Programa ID: {programa_id}, Estudiante ID: {estudiante_id}")
        
        if programa_id is not None and estudiante_id is not None:
            try:
                # Obtener el programa por su ID
                programa = Programa.objects.get(procod=programa_id)
                
                # Obtener el estudiante por su ID
                estudiante = EstudianteUser.objects.get(email=estudiante_id)
                
                # Obtener los registros de examen asociados al programa y al estudiante
                registros_examen = RegistroExamenPrograma.objects.filter(
                    regexaproprocod=programa,  # Filtrar por programa
                    regexaproestcod=estudiante    # Filtrar por estudiante
                )
                return registros_examen
            
            except Programa.DoesNotExist:
                return RegistroExamenPrograma.objects.none()
            
            except EstudianteUser.DoesNotExist:
                return RegistroExamenPrograma.objects.none()
            
        else:
            return RegistroExamenPrograma.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response(
                {"detail": "No se encontraron registros de exámenes para este programa y estudiante."},
                status=status.HTTP_404_NOT_FOUND
            )
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
    serializer_class = EstudianteUserSerializerList
    #permission_classes = [IsAuthenticated]

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




