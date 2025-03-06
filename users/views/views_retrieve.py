from rest_framework.generics import (
    RetrieveAPIView
)
from ..serializers_list_retrieve import *
from ..serializers import *


class EstudianteUserRetrieveAPIView(RetrieveAPIView):
    queryset = EstudianteUser.objects.all()
    serializer_class = EstudianteUserSerializerList