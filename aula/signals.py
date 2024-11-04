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


# signal para actualizar porcentaje de avance de u programa
@receiver(post_save, sender=RegistroExamen)
def actualizar_porcentaje_avance(sender, instance, created, **kwargs):
    # Obtener el programa y el estudiante del registro de examen
    estudiante = instance.regexaestcod
    programa = instance.regexaestprocod

    # Obtener la nota del programa asociada
    nota_programa, created = NotaPrograma.objects.get_or_create(
        notproestcod=estudiante,
        notproprocod=programa,
    )

    # Calcular el porcentaje de avance
    total_examenes = Examen.objects.filter(curso__programa=programa).count()
    examenes_completos = RegistroExamen.objects.filter(
        regexaestcod=estudiante,
        regexaestprocod=programa,
        regexapun__gte=70  # Asumiendo que regexapun es el puntaje
    ).count()

    # Actualizar el porcentaje de avance en NotaPrograma
    if total_examenes > 0:
        nota_programa.notpropor = (examenes_completos / total_examenes) * 100
    else:
        nota_programa.notpropor = 0

    nota_programa.save()


# Signal para verificar si se ha finalizado un programa
@receiver(post_save, sender=RegistroExamen)
def verificar_finalizacion_programa(sender, instance, **kwargs):
    # Obtener el estudiante y el programa del registro de examen
    estudiante = instance.regexaestcod
    programa = instance.regexaestprocod

    try:
        # Obtener la matrícula asociada
        matricula = Matricula.objects.get(matestcod=estudiante, matprocod=programa)

        # Obtener todos los exámenes del programa
        examenes = Examen.objects.filter(curso__programa=programa)

        # Verificar si todos los exámenes han sido completados y tienen notas >= 70
        todos_completos = all(
            RegistroExamen.objects.filter(regexaexacod=examen, regexaestcod=estudiante, regexaestprocod=programa).exists() and
            RegistroExamen.objects.get(regexaexacod=examen, regexaestcod=estudiante, regexaestprocod=programa).regexapun >= 70
            for examen in examenes
        )

        # Actualizar el campo finalizado en la matrícula
        matricula.matter = todos_completos
        matricula.save()

    except Matricula.DoesNotExist:
        # Manejar el caso donde no se encuentra la matrícula, si es necesario
        pass