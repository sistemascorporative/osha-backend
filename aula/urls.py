from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token

#from .views.views import login
from .views.views_create import *
from .views.views_list import *
from .views.views_retrieve import *
from .views.views_update import *
from .views.views_destroy import *

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('docs/', include_docs_urls(title="Aula API")),
    
    # Login
    
    #path("auth/", include('djoser.urls')),
    #path("auth/", include('djoser.urls.jwt')),
    
    #path('login/', login, name='login'),
    
    # List
    
    path('estado-registro/', EstadoRegistroListAPIView.as_view(), name='estado-regitro-list'),
    path('estudiante/', EstudianteListAPIView.as_view(), name='estudiante-list'),
    path('programa/', ProgramaListAPIView.as_view(), name='programa-list'),
    path('curso/', CursoListAPIView.as_view(), name='curso-list'),
    path('modulo/', ModuloListAPIView.as_view(), name='modulo-list'),
    path('examen/', ExamenListAPIView.as_view(), name='examen-list'),
    path('pregunta/', PreguntaListAPIView.as_view(), name='pregunta-list'),
    path('alternativa/', AlternativaListAPIView.as_view(), name='alternativa-list'),
    path('respuesta/', RespuestaListAPIView.as_view(), name='respuesta-list'),
    path('matricula/', MatriculaListAPIView.as_view(), name='matricula-list'),
    path('nota-curso/',RegistroCursoListAPIView.as_view(), name='nota-curso-list'),
    path('nota-programa/', NotaProgramaListAPIView.as_view(), name='nota-programa-list'),
    
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
    path('matricula/create/', MatriculaCreateAPIView.as_view(), name='matricula-create'),
    path('nota-curso/create/', RegistroCursoCreateAPIView.as_view(), name='nota-curso-create'),
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
    path('matricula/<int:pk>/', MatriculaRetrieveAPIView.as_view(), name='matricula-detail'),
    path('nota-curso/<int:pk>/', RegistroCursoRetrieveAPIView.as_view(), name='nota-curso-detail'),
    path('nota-programa/<int:pk>/', NotaProgramaRetrieveAPIView.as_view(), name='nota-programa-detail'),
    
    # Update
    
    path('estado-registro/<int:pk>/update/', EstadoRegistroUpdateAPIView.as_view(), name='estado-registro-update'),
    path('estudiante/<int:pk>/update/', EstudianteUpdateAPIView.as_view(), name='estudiante-update'),
    path('programa/<int:pk>/update/', ProgramaUpdateAPIView.as_view(), name='programa-update'),
    path('curso/<int:pk>/update/', CursoUpdateAPIView.as_view(), name='curso-update'),
    path('modulo/<int:pk>/update/', ModuloUpdateAPIView.as_view(), name='modulo-update'),
    path('examen/<int:pk>/update/', ExamenUpdateAPIView.as_view(), name='examen-update'),
    path('pregunta/<int:pk>/update/', PreguntaUpdateAPIView.as_view(), name='pregunta-update'),
    path('alternativa/<int:pk>/update/', AlternativaUpdateAPIView.as_view(), name='alternativa-update'),
    path('respuesta/<int:pk>/update/', RespuestaUpdateAPIView.as_view(), name='respuesta-update'),
    path('matricula/<int:pk>/update/', MatriculaUpdateAPIView.as_view(), name='matricula-update'),
    path('nota-curso/<int:pk>/update/', RegistroCursoUpdateAPIView.as_view(), name='nota-curso-update'),
    path('nota-programa/<int:pk>/update/', NotaProgramaUpdateAPIView.as_view(), name='nota-programa-update'),
    
    # Delete
    
    path('estado-registro/<int:pk>/delete/', EstadoRegistroDestroyAPIView.as_view(), name='estado-registro-delete'),
    path('estudiante/<int:pk>/delete/', EstudianteDestroyAPIView.as_view(), name='estudiante-delete'),
    path('programa/<int:pk>/delete/', ProgramaDestroyAPIView.as_view(), name='programa-delete'),
    path('curso/<int:pk>/delete/', CursoDestroyAPIView.as_view(), name='curso-delete'),
    path('modulo/<int:pk>/delete/', ModuloDestroyAPIView.as_view(), name='modulo-delete'),
    path('examen/<int:pk>/delete/', ExamenDestroyAPIView.as_view(), name='examen-delete'),
    path('pregunta/<int:pk>/delete/', PreguntaDestroyAPIView.as_view(), name='pregunta-delete'),
    path('alternativa/<int:pk>/delete/', AlternativaDestroyAPIView.as_view(), name='alternativa-delete'),
    path('respuesta/<int:pk>/delete/', RespuestaDestroyAPIView.as_view(), name='respuesta-delete'),
    path('matricula/<int:pk>/delete/', MatriculaDestroyAPIView.as_view(), name='matricula-delete'),
    path('nota-curso/<int:pk>/delete/', RegistroCursoDestroyAPIView.as_view(), name='nota-curso-delete'),
    path('nota-programa/<int:pk>/delete/', NotaProgramaDestroyAPIView.as_view(), name='nota-programa-delete'),
]
