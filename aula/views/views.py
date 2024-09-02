from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers_list_retrieve import RespuestaSerializerList
from ..models import Examen, Programa, EstudianteUser, Pregunta, Alternativa, Respuesta


class GuardarRespuestasAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        respuestas_data = request.data.get('respuestas', [])  # Lista de respuestas
        examen_id = request.data.get('examenId')
        programa_id = request.data.get('programaId')
        estudiante_id = request.user.id  # Asumimos que el usuario está autenticado
        
        # Validación de datos recibidos
        if not respuestas_data:
            return Response({"detail": "No se han proporcionado respuestas."}, status=status.HTTP_400_BAD_REQUEST)
        if not examen_id:
            return Response({"detail": "El ID del examen es requerido."}, status=status.HTTP_400_BAD_REQUEST)
        if not programa_id:
            return Response({"detail": "El ID del programa es requerido."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            examen = Examen.objects.get(pk=examen_id)
        except Examen.DoesNotExist:
            return Response({"detail": "El examen no existe."}, status=status.HTTP_404_NOT_FOUND)

        try:
            programa = Programa.objects.get(pk=programa_id)
        except Programa.DoesNotExist:
            return Response({"detail": "El programa no existe."}, status=status.HTTP_404_NOT_FOUND)

        try:
            estudiante = EstudianteUser.objects.get(pk=estudiante_id)
        except EstudianteUser.DoesNotExist:
            return Response({"detail": "El estudiante no existe."}, status=status.HTTP_404_NOT_FOUND)

        # Obtener el número total de preguntas en el examen
        total_preguntas = Pregunta.objects.filter(preexacod=examen).count()
        
        # Calcular la puntuación por cada respuesta correcta
        puntuacion_por_respuesta_correcta = 100.00 / total_preguntas if total_preguntas > 0 else 0.0
        
        for pregunta_id, alternativa_id in respuestas_data.items():
            try:
                pregunta = Pregunta.objects.get(pk=pregunta_id)
            except Pregunta.DoesNotExist:
                return Response({"detail": f"La pregunta con ID {pregunta_id} no existe."}, status=status.HTTP_404_NOT_FOUND)

            try:
                alternativa = Alternativa.objects.get(pk=alternativa_id)
            except Alternativa.DoesNotExist:
                return Response({"detail": f"La alternativa con ID {alternativa_id} no existe."}, status=status.HTTP_404_NOT_FOUND)
            
            # Calcular la puntuación según la lógica del negocio
            puntuacion = puntuacion_por_respuesta_correcta if alternativa.altcor else 0.0
            
            # Crear la respuesta
            respuesta = Respuesta(
                respun=puntuacion,
                resestcod=estudiante,
                resexacod=examen,
                resprecod=pregunta,
                resaltcod=alternativa,
                resprocod=programa,
            )
            respuesta.save()
        
        return Response({"message": "Respuestas guardadas con éxito."}, status=status.HTTP_201_CREATED)

