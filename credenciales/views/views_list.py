from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from ..serializers_list_retrieve import *
from ..serializers import *
from ..models import *
from django.shortcuts import get_object_or_404
from users.models import EstudianteUser, UserSimple

#ListAPIViews

"""
Endpoint para obtener todos los credenciales de programas matriculados por estudiante pk
"""
class CredencialProgramaMatriculadoByPkListView(ListAPIView):
    serializer_class = CredencialProgramaMatriculadoSerializerList

    def get_queryset(self):
        id = self.kwargs.get('pk')
        return CredencialProgramaMatriculado.objects.filter(crepromatprocod__matproestcod=id)


"""
Endpoint para obtener todos los credenciales de programas por estudiante pk
"""
class CredencialProgramaByPkListView(ListAPIView):
    serializer_class = CredencialProgramaSerializerList

    def get_queryset(self):
        id = self.kwargs.get('pk')
        return CredencialPrograma.objects.filter(creproestcod=id)


"""
Endpoint para obtener todos los certificados de cursos matriculados por estudiante pk
"""
class CertificadoCursoMatriculadoByPkListView(ListAPIView):
    serializer_class = CertificadoCursoMatriculadoSerializerList

    def get_queryset(self):
        id = self.kwargs.get('pk')
        return CertificadoCursoMatriculado.objects.filter(cercurmatcurcod__matcurestcod=id)


"""
Endpoint para obtener todos los certificados de cursos por estudiante pk
"""
class CertificadoCursoByPkListView(ListAPIView):
    serializer_class = CertificadoCursoSerializerList

    def get_queryset(self):
        id = self.kwargs.get('pk')
        return CertificadoCurso.objects.filter(cercurestcod=id)





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
        estudiante = get_object_or_404(UserSimple, email=email)
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
        estudiante = get_object_or_404(UserSimple, email=email)
        return CertificadoCurso.objects.filter(cercurestcod=estudiante)


"""
Endpoint para obtener todos los credenciales de programas matriculados por estudiante documento de identidad
"""
class CredencialProgramaMatriculadoByDocIdListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CredencialProgramaMatriculadoSerializerListMin

    def get_queryset(self):
        docId = self.kwargs.get('documento_identidad')
        estudiante = get_object_or_404(EstudianteUser, usuario__userdocide=docId)
        return CredencialProgramaMatriculado.objects.filter(crepromatprocod__matproestcod=estudiante)


"""
Endpoint para obtener todos los credenciales de programas por estudiante documento de identidad
"""
class CredencialProgramaByDocIdListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CredencialProgramaSerializerListMin

    def get_queryset(self):
        docId = self.kwargs.get('documento_identidad')
        estudiante = get_object_or_404(UserSimple, userdocide=docId)
        return CredencialPrograma.objects.filter(creproestcod=estudiante)


"""
Endpoint para obtener todos los certificados de cursos matriculados por estudiante documento de identidad
"""
class CertificadoCursoMatriculadoByDocIdListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificadoCursoMatriculadoSerializerListMin

    def get_queryset(self):
        docId = self.kwargs.get('documento_identidad')
        estudiante = get_object_or_404(EstudianteUser, usuario__userdocide=docId)
        return CertificadoCursoMatriculado.objects.filter(cercurmatcurcod__matcurestcod=estudiante)


"""
Endpoint para obtener todos los certificados de cursos por estudiante documento de identidad
"""
class CertificadoCursoByDocIdListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificadoCursoSerializerListMin

    def get_queryset(self):
        docId = self.kwargs.get('documento_identidad')
        estudiante = get_object_or_404(UserSimple, userdocide=docId)
        return CertificadoCurso.objects.filter(cercurestcod=estudiante)


"""
Endpoint para obtener todos los credenciales de programas matriculados por estudiante por codigo osha
"""
class CredencialProgramaMatriculadoByCodOshListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CredencialProgramaMatriculadoSerializerListMin

    def get_queryset(self):
        userCodOsh = self.kwargs.get('usercodosh')
        estudiante = get_object_or_404(EstudianteUser, usuario__usercodosh=userCodOsh)
        return CredencialProgramaMatriculado.objects.filter(crepromatprocod__matproestcod=estudiante)


"""
Endpoint para obtener todos los credenciales de programas por estudiante por codigo osha
"""
class CredencialProgramaByCodOshListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CredencialProgramaSerializerListMin

    def get_queryset(self):
        userCodOsh = self.kwargs.get('usercodosh')
        estudiante = get_object_or_404(UserSimple, usercodosh=userCodOsh)
        return CredencialPrograma.objects.filter(creproestcod=estudiante)


"""
Endpoint para obtener todos los certificados de cursos matriculados por estudiante por codigo osha
"""
class CertificadoCursoMatriculadoByCodOshListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificadoCursoMatriculadoSerializerListMin

    def get_queryset(self):
        userCodOsh = self.kwargs.get('usercodosh')
        estudiante = get_object_or_404(EstudianteUser, usuario__usercodosh=userCodOsh)
        return CertificadoCursoMatriculado.objects.filter(cercurmatcurcod__matcurestcod=estudiante)


"""
Endpoint para obtener todos los certificados de cursos por estudiante por codigo osha
"""
class CertificadoCursoByCodOshListView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = CertificadoCursoSerializerListMin

    def get_queryset(self):
        userCodOsh = self.kwargs.get('usercodosh')
        estudiante = get_object_or_404(UserSimple, usercodosh=userCodOsh)
        return CertificadoCurso.objects.filter(cercurestcod=estudiante)