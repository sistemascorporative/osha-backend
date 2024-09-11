from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Avg
from ..serializers_list_retrieve import RespuestaSerializerList
from ..models import Examen, Programa, EstudianteUser, Pregunta, Alternativa, Respuesta, RegistroExamen, EstadoExamen, NotaPrograma


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
        
        puntuacion_total = 0.0
        
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
            puntuacion_total += puntuacion
            
            # Verificar si ya existe un registro de respuesta para esta pregunta
            respuesta_existente = Respuesta.objects.filter(
                resestcod=estudiante,
                resexacod=examen,
                resprecod=pregunta,
                resprocod=programa,
            ).first()

            if respuesta_existente:
                # Actualizar la respuesta existente
                respuesta_existente.resaltcod = alternativa
                respuesta_existente.respun = puntuacion
                respuesta_existente.save()
            else:
                # Crear una nueva respuesta si no existe
                nueva_respuesta = Respuesta(
                    respun=puntuacion,
                    resestcod=estudiante,
                    resexacod=examen,
                    resprecod=pregunta,
                    resaltcod=alternativa,
                    resprocod=programa,
                )
                nueva_respuesta.save()
        
        # Obtener el registro del examen para el estudiante y el curso
        registro_examen, created = RegistroExamen.objects.get_or_create(
            regexaestcod=estudiante,
            regexaexacod=examen,
            regexaestprocod=programa,
        )
        
        # Actualizar la puntuación total y el número de intentos
        registro_examen.regexapun = puntuacion_total
        registro_examen.regexaint += 1
        
        # Actualizar el estado del examen según la puntuación obtenida
        estado_aprobado = EstadoExamen.objects.get(estexanom="Aprobado")
        estado_desaprobado = EstadoExamen.objects.get(estexanom="Reprobado")
        if puntuacion_total >= 85.0:
            registro_examen.regexaestexacod = estado_aprobado
        else:
            registro_examen.regexaestexacod = estado_desaprobado

        registro_examen.save()
        
        # Calcular el promedio de todas las puntuaciones de exámenes del estudiante en el programa
        registros_examen = RegistroExamen.objects.filter(
            regexaestcod=estudiante,
            regexaestprocod=programa
        )
        promedio_puntuacion = registros_examen.aggregate(promedio=Avg('regexapun'))['promedio']
        
        # Actualizar el campo notpropun en el modelo NotaPrograma
        nota_programa = NotaPrograma.objects.get(notproestcod=estudiante, notproprocod=programa)
        nota_programa.notpropun = promedio_puntuacion
        nota_programa.save()
        
        return Response({"message": "Respuestas guardadas o actualizadas con éxito."}, status=status.HTTP_200_OK)

