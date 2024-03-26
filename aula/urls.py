from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

from .views.views_create import *
from .views.views_list import *
from .views.views_retrieve import *
from .views.views_update import *
from .views.views_destroy import *

urlpatterns = [
    path('docs/', include_docs_urls(title="Aula API")),
    
    # List
    
    path('estado-registro/', EstadoRegistroListAPIView.as_view(), name='estado-regitro-list'),
    path('estudiante/', EstudianteListAPIView.as_view(), name='estudiante-list/'),
    path('programa/', ProgramaListAPIView.as_view(), name='programa-list/'),
    path('curso/', CursoListAPIView.as_view(), name='curso-list/'),
    path('modulo/', ModuloListAPIView.as_view(), name='modulo-list/'),
    path('examen/', ExamenListAPIView.as_view(), name='examen-list/'),
    path('pregunta/', PreguntaListAPIView.as_view(), name='pregunta-list/'),
    path('alternativa/', AlternativaListAPIView.as_view(), name='alternativa-list/'),
    path('respuesta/', RespuestaListAPIView.as_view(), name='respuesta-list/'),
    path('nota-curso/', NotaCursoListAPIView.as_view(), name='nota-curso-list/'),
    path('nota-programa/', NotaProgramaListAPIView.as_view(), name='nota-programa-list/'),
    
    # Create
    
    path('estado-registro/create/', EstadoRegistroCreateAPIView.as_view(), name='estado-registro-create'),
    path('estudiante/create/', EstudianteCreateAPIView.as_view(), name='estudiante-create'),
    path('programa/create/', ProgramaCreateAPIView.as_view(), name='programa-create'),
    path('curso/create/', CursoCreateAPIView.as_view(), name='curso-create'),
    path('modulo/create/', ModuloCreateAPIView.as_view(), name='modulo-create'),
    path('examen/create/', ExamenCreateAPIView.as_view(), name='examen-create'),
    path('pregunta/create/', PreguntaCreateAPIView.as_view(), name='pregunta-create'),
    path('alternativa/create/', AlternativaCreateAPIView.as_view(), name='alternativa-create'),
    path('respuesta/create/', RespuestaCreateAPIView.as_view(), name='respuesta-create'),
    path('nota-curso/create/', NotaCursoCreateAPIView.as_view(), name='nota-curso-create'),
    path('nota-programa/create/', NotaProgramaCreateAPIView.as_view(), name='nota-programa-create'),
    
    # Detail
    
    path('estado-registro/<int:pk>/', EstadoRegistroRetrieveAPIView.as_view(), name='estado-registro-detail'),
    path('estudiante/<int:pk>/', EstudianteRetrieveAPIView.as_view(), name='estudiante-detail'),
    path('programa/<int:pk>/', ProgramaRetrieveAPIView.as_view(), name='programa-detail'),
    path('curso/<int:pk>/', CursoRetrieveAPIView.as_view(), name='curso-detail'),
    path('modulo/<int:pk>/', ModuloRetrieveAPIView.as_view(), name='modulo-detail'),
    path('examen/<int:pk>/', ExamenRetrieveAPIView.as_view(), name='examen-detail'),
    path('pregunta/<int:pk>/', PreguntaRetrieveAPIView.as_view(), name='pregunta-detail'),
    path('alternativa/<int:pk>/', AlternativaRetrieveAPIView.as_view(), name='alternativa-detail'),
    path('respuesta/<int:pk>/', RespuestaRetrieveAPIView.as_view(), name='respuesta-detail'),
    path('nota-curso/<int:pk>/', NotaCursoRetrieveAPIView.as_view(), name='nota-curso-detail'),
    path('nota-programa/<int:pk>/', NotaProgramaRetrieveAPIView.as_view(), name='nota-programa-detail'),
    
    #
]
