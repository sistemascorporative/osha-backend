from django.db.models.signals import m2m_changed, post_save, post_delete, pre_save
from django.db.models import Avg, Count
from decimal import Decimal, ROUND_HALF_UP
from django.dispatch import receiver
from .models import (
    Programa, Modulo, Examen, Pregunta, EstadoExamen,
    MatriculaPrograma, MatriculaCurso,
    RespuestaExamenPrograma, RegistroExamenPrograma, RegistroExamenCurso
)
import logging


# Configuración del logger
logger = logging.getLogger(__name__)


"""
Actualizar el promedio de matricula de un programa y si ha finalizado el programa
"""
@receiver(post_save, sender=RespuestaExamenPrograma)
def update_matricula_programa(sender, instance, **kwargs):
    estudiante = instance.resproestcod
    programa = instance.resproprocod

    # Obtener todas las respuestas del estudiante en ese programa
    respuestas = RespuestaExamenPrograma.objects.filter(
        resproestcod=estudiante,
        resproprocod=programa
    )

    # Calcular el promedio de puntajes (ignorando los nulos)
    promedio = respuestas.aggregate(promedio=Avg('respropun'))['promedio'] or 0.00
    promedio_decimal = Decimal(promedio).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # Número de respuestas del estudiante en el programa
    num_respuestas = respuestas.count()

    # Número de cursos en el programa
    num_cursos = programa.cursos.count()

    # Obtener la matrícula del programa
    try:
        matricula = MatriculaPrograma.objects.get(
            matproestcod=estudiante,
            matproprocod=programa
        )

        # Actualizar el promedio
        matricula.matpropun = promedio_decimal

        # Verificar si el estudiante ha terminado el programa
        if promedio_decimal >= Decimal("70.00") and num_respuestas == num_cursos:
            matricula.matproter = True

        matricula.save()

    except MatriculaPrograma.DoesNotExist:
        pass



"""
Actualizar número de cursos en la tabla Programa
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
Actualiza el número de preguntas de la tabla Examen cuando crea, actualiza o elimina una pregunta
"""
@receiver(post_save, sender=Pregunta)
@receiver(post_delete, sender=Pregunta)
def update_pregunta_count(sender, instance, **kwargs):
    examen = instance.preexacod
    examen.exanumpre = examen.pregunta_set.count()
    examen.save()



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
                    regexaproprocod=programa,
                    regexaproestcod=estudiante,
                    regexaproexacod=examen,
                    defaults={
                        'regexapropun': 0.00,
                        'regexaproint': 0,
                        'regexaproestexacod': estado_pendiente  # Asumiendo que 2 es el estado inicial del examen
                    }
                )
            except Examen.DoesNotExist:
                print(f"No existe examen para el curso: {curso.curnom}")


"""
Signal para actualizar el estudiante en los registros de examen programa asociados a una matrícula de programa.
"""
@receiver(pre_save, sender=MatriculaPrograma)
def actualizar_estudiante_en_registro_examen_programa(sender, instance, **kwargs):
    try:
        if not instance.pk: # Es una nueva matrícula, no hay estudiante anterior
            return

        antigua = MatriculaPrograma.objects.get(pk=instance.pk)

        if antigua.matproestcod != instance.matproestcod:
            registros = RegistroExamenPrograma.objects.filter(
                regexaproprocod=instance.matproprocod,
                regexaproestcod=antigua.matproestcod
            )
            cantidad = registros.update(regexaproestcod=instance.matproestcod)

            logger.info(f"[Signal] {cantidad} registros de RegistroExamenPrograma actualizados: "
                        f"estudiante cambiado de {antigua.matproestcod.id} a {instance.matproestcod.id} "
                        f"para programa {instance.matproprocod.id}.")
    except Exception as e:
        logger.error(f"[Signal] Error al actualizar RegistroExamenPrograma al cambiar estudiante en MatriculaPrograma: {e}", exc_info=True)


"""
Signal para eliminar los registros de examen asociados a una matrícula de programa.
"""
@receiver(post_delete, sender=MatriculaPrograma)
def eliminar_registros_examen_programa(sender, instance, **kwargs):
    try:
        estudiante = instance.matproestcod
        programa = instance.matproprocod

        registros = RegistroExamenPrograma.objects.filter(
            regexaproestcod=estudiante,
            regexaproprocod=programa
        )

        cantidad_eliminada, detalles = registros.delete()
        logger.info(f"[Signal] Se eliminaron {cantidad_eliminada} registros de RegistroExamenPrograma "
                    f"relacionados con la matrícula (Est: {estudiante.id}, Prog: {programa.id}).")

    except Exception as e:
        logger.error(f"[Signal] Error al eliminar registros de RegistroExamenPrograma: {e}", exc_info=True)


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
                regexacurcurcod=instance.matcurcurcod,
                regexacurestcod=instance.matcurestcod,
                regexacurexacod=examen
            )
        except Examen.DoesNotExist:
            # Manejar el caso donde no existe un examen para el curso
            print(f"No se encontró examen para el curso {curso.curnom}")


"""
Signal para actualizar el estudiante cuando se haga una modificacion en la matrícula
"""
@receiver(pre_save, sender=MatriculaCurso)
def actualizar_estudiante_en_registro_examen_curso(sender, instance, **kwargs):
    try:
        if not instance.pk: # Es una nueva matrícula, no hay estudiante anterior
            return

        antigua = MatriculaCurso.objects.get(pk=instance.pk)

        if antigua.matcurestcod != instance.matcurestcod:
            # Filtrar todos los registros del curso con el estudiante anterior
            registros = RegistroExamenCurso.objects.filter(
                regexacurcurcod=instance.matcurcurcod,
                regexacurestcod=antigua.matcurestcod
            )
            cantidad = registros.update(regexacurestcod=instance.matcurestcod)

            logger.info(f"[Signal] {cantidad} registros de RegistroExamenCurso actualizados: "
                        f"estudiante cambiado de {antigua.matcurestcod.id} a {instance.matcurestcod.id} "
                        f"para curso {instance.matcurcurcod.id}.")
    except Exception as e:
        logger.error(f"[Signal] Error actualizando RegistroExamenCurso al cambiar estudiante en MatriculaCurso: {e}", exc_info=True)


"""
Signal para eliminar los registros de examen asociados a una matrícula de curso.
"""
@receiver(post_delete, sender=MatriculaCurso)
def eliminar_registros_examen_curso(sender, instance, **kwargs):
    try:
        estudiante = instance.matcurestcod
        curso = instance.matcurcurcod

        registros = RegistroExamenCurso.objects.filter(
            regexacurestcod=estudiante,
            regexacurcurcod=curso
        )

        cantidad_eliminada, _ = registros.delete()
        logger.info(f"[Signal] Se eliminaron {cantidad_eliminada} registros de RegistroExamenCurso "
                    f"relacionados con la matrícula eliminada (Est: {estudiante.id}, Curso: {curso.id}).")

    except Exception as e:
        logger.error(f"[Signal] Error al eliminar registros de RegistroExamenCurso: {e}", exc_info=True)


"""
signal para actualizar porcentaje de avance de un programa
"""


"""
Verificar si se ha finalizado un programa
"""
