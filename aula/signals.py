from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from .models import Programa, Modulo, Matricula, Examen, EstadoExamen, RegistroExamen


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

@receiver(post_save, sender=Matricula)
def crear_registros_examen(sender, instance, created, **kwargs):
    if created:
        programa = instance.matprocod
        estudiante = instance.matestcod
        exámenes = Examen.objects.filter(exacurcod__in=programa.cursos.all())
        # Suponiendo que el estado "Pendiente" existe
        estado_pendiente, created = EstadoExamen.objects.get_or_create(estexanom="Pendiente")
        
        for examen in exámenes:
            RegistroExamen.objects.create(
                regexapun=0.00,  # Puedes ajustar este valor según sea necesario
                regexaint=0,
                regexaestexacod=estado_pendiente,
                regexaestcod=estudiante,
                regexaexacod=examen
            )