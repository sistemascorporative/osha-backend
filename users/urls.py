from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.views import PublicUserViewSet, EstudianteUserByEmailAPIView
from .views.views_retrieve import EstudianteUserRetrieveAPIView


urlpatterns = [
    path('auth/users/', PublicUserViewSet.as_view({'post': 'create'}), name='user-create'),  # Registro
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
    # Detail
    
    #path('estudiante/<int:pk>/', EstudianteUserRetrieveAPIView.as_view(), name='estudiante-detail'),
    path('estudiante/<str:email>/', EstudianteUserByEmailAPIView.as_view(), name='estudiante-detail'),
]