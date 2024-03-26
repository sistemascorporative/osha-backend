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
    
    # Create
    path('estreg/create', EstadoRegistroCreateAPIView.as_view(), name='estado-registro-create'),
    path('estudiante/create', EstudianteCreateAPIView.as_view(), name='estudiante-create'),
    path('programa/create', ProgramaCreateAPIView.as_view(), name='programa-create'),
    path('curso/create', CursoCreateAPIView.as_view(), name='curso-create'),
    path('modulo/create', ModuloCreateAPIView.as_view(), name='modulo-create'),
    path('examen/create', ExamenCreateAPIView.as_view(), name='examen-create'),
    path('pregunta/create', PreguntaCreateAPIView.as_view(), name='pregunta-create'),
    path('alternativa/create', AlternativaCreateAPIView.as_view(), name='alternativa-create'),
    path('respuesta/create', RespuestaCreateAPIView.as_view(), name='respuesta-create'),
]
