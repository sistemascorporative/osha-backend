from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings


class ContactoAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        fullname = request.data.get('fullname')
        email = request.data.get('email')
        phone = request.data.get('phone')
        age = request.data.get('age')
        country = request.data.get('country')
        degree = request.data.get('degree')
        programOsha = request.data.get('programOsha')
        information = request.data.get('information')

        # Extrae solo el label
        programOsha_label = programOsha.get('label') if isinstance(programOsha, dict) else programOsha
        
        try:
            send_mail(
                subject=f"SOLICITUD DE INFORMACIÓN DE {fullname}",
                message=(
                    f"Nombre: {fullname}\n"
                    f"Email: {email}\n"
                    f"Teléfono: {phone}\n"
                    f"Edad: {age}\n"
                    f"País: {country}\n"
                    f"Grado de instrucción: {degree}\n"
                    f"Programa osha de interes: {programOsha_label}\n\n"
                    f"Mensaje:\n{information}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["info@osha.es", "contacto@osha.es", "oshaperu2021@gmail.com"],
                fail_silently=False,
            )
            return Response({'detail': 'Correo enviado'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)