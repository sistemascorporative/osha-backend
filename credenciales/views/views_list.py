from rest_framework.generics import ListAPIView
from ..serializers_list_retrieve import *
from ..serializers import *
from ..models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


#ListAPIViews


"""
Endpoint para obtener todos los credenciales de programas matriculados por estudiante emaill
"""
class CredencialProgramaMatriculadoByEmailListView(ListAPIView):
    serializer_class = CredencialProgramaMatriculadoSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        return CredencialProgramaMatriculado.objects.filter(crepromatprocod__estudiante=estudiante)


"""
Endpoint para obtener todos los credenciales de programas por estudiante emaill
"""
class CredencialProgramaByEmailListView(ListAPIView):
    serializer_class = CredencialProgramaSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        return CredencialPrograma.objects.filter(creproestcod=estudiante)


"""
Endpoint para obtener todos los certificados de cursos matriculados por estudiante email
"""
class CertificadoCursoMatriculadoByEmailListView(ListAPIView):
    serializer_class = CertificadoCursoMatriculadoSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        matriculas_curso = MatriculaCurso.objects.filter(estudiante=estudiante)
        return CertificadoCursoMatriculado.objects.filter(cercurmatcurcod__in=matriculas_curso)


"""
Endpoint para obtener todos los certificados de cursos por estudiante email
"""
class CertificadoCursoByEmailListView(ListAPIView):
    serializer_class = CertificadoCursoSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        return CertificadoCurso.objects.filter(cercurestcod=estudiante)