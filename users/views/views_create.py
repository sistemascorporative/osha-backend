from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db import transaction
from ..models import UserSimple, EstudianteUser
from ..serializers import RegisterUserSerializer


class RegisterUserView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    user_simple = UserSimple.objects.create(
                        usernom=serializer.validated_data['nombre'],
                        userape=serializer.validated_data['apellido'],
                        userdocide=serializer.validated_data['dni'],
                        userpai=serializer.validated_data['pais'],
                        userciu=serializer.validated_data['ciudad'],
                        userdir=serializer.validated_data['direccion']
                    )
                    estudiante_user = EstudianteUser.objects.create(
                        usuario=user_simple,
                        email=serializer.validated_data['email'],
                        is_active=False
                    )
                    estudiante_user.set_password(serializer.validated_data['password'])
                    estudiante_user.save()
                return Response({"message": "Usuario registrado exitosamente. Esperando activación."}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
