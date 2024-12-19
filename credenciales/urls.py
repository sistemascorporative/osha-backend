from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

from .views.views_list import *



urlpatterns = [
    
    # List
    
    path('credenciales/programa/matriculado/by-email/<str:estudiante_email>/', CredencialProgramaMatriculadoByEmailListView.as_view(), name='credencial-programa-by-email'),
    path('credenciales/programa/by-email/<str:estudiante_email>/', CredencialProgramaByEmailListView.as_view(), name='credencial-programa-by-email'),
    path('certificados/curso/matriculado/by-email/<str:estudiante_email>/', CertificadoCursoMatriculadoByEmailListView.as_view(), name='certificado-curso-matriculado-by-email'),
    path('certificados/curso/by-email/<str:estudiante_email>/', CertificadoCursoByEmailListView.as_view(), name='certificado-curso-by-email'),
]
