from django.shortcuts import render
from users.models import EstudianteUser

# Create your views here.

"""
Endpoint para obtener todos los certificados de cursos por estudiante email
"""
class CertificadoCursoByEmailListView(ListAPIView):
    serializer_class = CertificadoCursoSerializerList

    def get_queryset(self):
        email = self.kwargs.get('estudiante_email')
        estudiante = get_object_or_404(EstudianteUser, email=email)
        return CertificadoCurso.objects.filter(cercurestcod=estudiante)