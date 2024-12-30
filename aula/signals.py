from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from .models import *
import logging


# Configuración del logger
logger = logging.getLogger(__name__)


"""
Actualizar numero de cursos en la tabla Programa
"""
@receiver(m2m_changed, sender=Programa.cursos.through)
def update_curso_count(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.pronumcur = instance.cursos.count()
        instance.save()


"""
Actualiza el número de modulos en la tabla Curso crea, actualiza o elimina un modulo
"""
@receiver(post_save, sender=Modulo)
@receiver(post_delete, sender=Modulo)
def update_modulo_count(sender, instance, **kwargs):
    curso = instance.modcurcod
    curso.curnummod = curso.modulo_set.count()
    curso.save()


"""
Actualiza el número de preguntas de la tabla Exmen cuando crea, actualiza o elimina una pregunta
"""
@receiver(post_save, sender=Pregunta)
@receiver(post_delete, sender=Pregunta)
def update_pregunta_count(sender, instance, **kwargs):
    examen = instance.preexacod
    examen.exanumpre = examen.pregunta_set.count()
    examen.save()


"""
Crear y eliminar nota programa
"""

"""
Crear registro de examen despeus de matricula
eliminar registros de examen
"""



"""
Signal para crear registros de exámenes para todos los cursos de un programa
cuando se realiza una matrícula para el programa.
"""
@receiver(post_save, sender=MatriculaPrograma)
def crear_registros_examen_por_programa(sender, instance, created, **kwargs):
    if created:
        programa = instance.matproprocod  # Programa asociado a la matrícula
        estudiante = instance.matproestcod  # Estudiante asociado a la matrícula
        # Suponiendo que el estado "Pendiente" existe
        estado_pendiente, created = EstadoExamen.objects.get_or_create(estexanom="Pendiente")
        # Obtener los cursos del programa
        cursos = programa.cursos.all()
        # Iterar sobre los cursos y crear registros de examen
        for curso in cursos:
            try:
                examen = Examen.objects.get(exacurcod=curso)
                RegistroExamenPrograma.objects.get_or_create(
                    regexapromatprocod=instance,
                    regexaproexacod=examen,
                    defaults={
                        'regexapropun': 0.00,
                        'regexaproint': 0,
                        'regexaproestexacod': estado_pendiente  # Asumiendo que 1 es el estado inicial del examen
                    }
                )
            except Examen.DoesNotExist:
                print(f"No existe examen para el curso: {curso.curnom}")


"""
Signal para eliminar los registros de examen asociados a una matrícula de programa.
"""
@receiver(post_delete, sender=MatriculaPrograma)
def eliminar_registros_examen_programa(sender, instance, **kwargs):
    try:
        # Obtener todas las matrículas de curso asociadas al programa
        matriculas_curso = MatriculaCurso.objects.filter(
            matcurestcod=instance.matproestcod,  # Estudiante asociado
            matcurcurcod__in=instance.matproprocod.cursos.all()  # Cursos del programa
        )
        # Eliminar los registros de examen asociados a las matrículas de curso
        total_eliminados = 0
        for matricula_curso in matriculas_curso:
            registros_eliminados = RegistroExamenCurso.objects.filter(
                regexacurmatcurcod=matricula_curso
            ).delete()
            total_eliminados += registros_eliminados[0]
        logger.info(
            f"Se eliminaron {total_eliminados} registro(s) de examen asociados al programa {instance.matproprocod.pronom}."
        )
    except Exception as e:
        logger.error(
            f"Error al eliminar los registros de examen para la matrícula de programa {instance.matprocod}: {e}"
        )


"""
Signal para crear un registro de examen curso para una matrícula de curso
"""
@receiver(post_save, sender=MatriculaCurso)
def crear_registro_examen_curso(sender, instance, created, **kwargs):
    if created:
        curso = instance.matcurcurcod
        try:
            # Buscar el examen asociado al curso
            examen = Examen.objects.get(exacurcod=curso)
            estado_pendiente, created = EstadoExamen.objects.get_or_create(estexanom="Pendiente")
            RegistroExamenCurso.objects.create(
                regexacurpun=0.0,  # Puntuación inicial
                regexacurint=0,  # Número de intentos inicial
                regexacurestexacod=estado_pendiente,
                regexacurmatcurcod=instance,
                regexacurexacod=examen
            )
        except Examen.DoesNotExist:
            # Manejar el caso donde no existe un examen para el curso
            print(f"No se encontró examen para el curso {curso.curnom}")


"""
Signal para eliminar los registros de examen asociados a una matrícula de curso.
"""
@receiver(post_delete, sender=MatriculaCurso)
def eliminar_registros_examen_curso(sender, instance, **kwargs):
    try:
        # Eliminar los registros de examen asociados a la matrícula
        registros_eliminados = RegistroExamenCurso.objects.filter(
            regexacurmatcurcod=instance
        ).delete()
        logger.info(
            f"Se eliminaron {registros_eliminados[0]} registro(s) de examen para la matrícula de curso {instance.matcurcod}."
        )
    except Exception as e:
        logger.error(
            f"Error al eliminar los registros de examen para la matrícula de curso {instance.matcurcod}: {e}"
        )


"""
signal para actualizar porcentaje de avance de u programa
"""


"""
Verificar si se ha finalizado un programa
"""