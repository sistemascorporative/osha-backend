from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from ..serializers_list_retrieve import *
from ..serializers import *
from ..models import *
from django.shortcuts import get_object_or_404
from users.models import EstudianteUser

#ListAPIViews


"""
Endpoint para obtener todos los credenciales de programas matriculados por estudiante emaill
"""
class CredencialProgramaMatriculadoByEmailListView(ListAPIView):
    serializer_class = CredencialProgramaMatriculadoSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        return CredencialProgramaMatriculado.objects.filter(crepromatprocod__matproestcod=estudiante)


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
        return CertificadoCursoMatriculado.objects.filter(cercurmatcurcod__matcurestcod=estudiante)


"""
Endpoint para obtener todos los certificados de cursos por estudiante email
"""
class CertificadoCursoByEmailListView(ListAPIView):
    serializer_class = CertificadoCursoSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, userdocide=email)
        return CertificadoCurso.objects.filter(cercurestcod=estudiante)


"""
Endpoint para obtener todos los credenciales de programas matriculados por estudiante documento de identidad
"""
class CredencialProgramaMatriculadoByDocIdListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CredencialProgramaMatriculadoSerializerList

    def get_queryset(self):
        docId = self.kwargs.get('documento_identidad')
        estudiante = get_object_or_404(EstudianteUser, userdocide=docId)
        return CredencialProgramaMatriculado.objects.filter(crepromatprocod__matproestcod=estudiante)


"""
Endpoint para obtener todos los credenciales de programas por estudiante documento de identidad
"""
class CredencialProgramaByDocIdListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CredencialProgramaSerializerList

    def get_queryset(self):
        docId = self.kwargs.get('documento_identidad')
        estudiante = get_object_or_404(EstudianteUser, userdocide=docId)
        return CredencialPrograma.objects.filter(creproestcod=estudiante)


"""
Endpoint para obtener todos los certificados de cursos matriculados por estudiante documento de identidad
"""
class CertificadoCursoMatriculadoByDocIdListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificadoCursoMatriculadoSerializerList

    def get_queryset(self):
        docId = self.kwargs.get('documento_identidad')
        estudiante = get_object_or_404(EstudianteUser, userdocide=docId)
        return CertificadoCursoMatriculado.objects.filter(cercurmatcurcod__matcurestcod=estudiante)


"""
Endpoint para obtener todos los certificados de cursos por estudiante documento de identidad
"""
class CertificadoCursoByDocIdListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificadoCursoSerializerList

    def get_queryset(self):
        docId = self.kwargs.get('documento_identidad')
        estudiante = get_object_or_404(EstudianteUser, userdocide=docId)
        return CertificadoCurso.objects.filter(cercurestcod=estudiante)
