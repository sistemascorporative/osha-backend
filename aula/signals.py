from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from .models import Programa, Modulo, Pregunta, Matricula, Examen, EstadoExamen, RegistroExamen, NotaPrograma


@receiver(m2m_changed, sender=Programa.cursos.through)
def update_curso_count(sender, instance, action, **kwargs):
    if action in ["post_add", "post_remove", "post_clear"]:
        instance.pronumcur = instance.cursos.count()
        instance.save()


@receiver(post_save, sender=Modulo)
@receiver(post_delete, sender=Modulo)
def update_modulo_count(sender, instance, **kwargs):
    curso = instance.modcurcod
    curso.curnummod = curso.modulo_set.count()
    curso.save()


@receiver(post_save, sender=Pregunta)
@receiver(post_delete, sender=Pregunta)
def update_pregunta_count(sender, instance, **kwargs):
    examen = instance.preexacod
    examen.exanumpre = examen.pregunta_set.count()
    examen.save()


@receiver(post_save, sender=Matricula)
def create_nota_programa(sender, instance, created, **kwargs):
    if created:
        NotaPrograma.objects.get_or_create(
            notproestcod=instance.matestcod,
            notproprocod=instance.matprocod,
            defaults={'notpropun': 0.0}  # Puntuación inicial predeterminada
        )


@receiver(post_delete, sender=Matricula)
def delete_nota_programa(sender, instance, **kwargs):
    # Intenta obtener el registro de NotaPrograma relacionado
    try:
        nota_programa = NotaPrograma.objects.get(
            notproestcod=instance.matestcod,
            notproprocod=instance.matprocod
        )
        nota_programa.delete()  # Eliminar el registro si se encuentra
    except NotaPrograma.DoesNotExist:
        # Maneja el caso donde no existe el registro, si es necesario
        pass


# Signal para crear registros de examen al crear una matrícula
@receiver(post_save, sender=Matricula)
def create_registro_examen(sender, instance, created, **kwargs):
    if created:
        estudiante = instance.matestcod
        programa = instance.matprocod
        # Suponiendo que el estado "Pendiente" existe
        estado_pendiente, created = EstadoExamen.objects.get_or_create(estexanom="Pendiente")
        # Obtener todos los cursos del programa
        cursos = programa.cursos.all()
        for curso in cursos:
            try:
                examen = Examen.objects.get(exacurcod=curso)
                RegistroExamen.objects.create(
                    regexapun=0.00,
                    regexaint=0,
                    regexaestcod=estudiante,
                    regexaestprocod=programa,
                    regexaexacod=examen,
                    regexaestexacod=estado_pendiente  # Ajusta esto según tu lógica de estado de examen
                )
            except Examen.DoesNotExist:
                # Manejar el caso donde no existe un examen para el curso
                pass


# Signal para eliminar registros de examen al eliminar una matrícula
@receiver(post_delete, sender=Matricula)
def delete_registro_examen(sender, instance, **kwargs):
    estudiante = instance.matestcod
    programa = instance.matprocod
    # Eliminar todos los registros de examen asociados al estudiante y al programa
    RegistroExamen.objects.filter(
        regexaestcod=estudiante,
        regexaestprocod=programa
    ).delete()