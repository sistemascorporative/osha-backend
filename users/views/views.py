from rest_framework.permissions import AllowAny
from djoser.views import UserViewSet

# Create your views here.

class PublicUserViewSet(UserViewSet):
    permission_classes = [AllowAny]