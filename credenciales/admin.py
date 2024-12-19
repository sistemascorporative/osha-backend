from django.contrib import admin
from .models import *



@admin.register(CredencialProgramaMatriculado)
class CredencialProgramaMatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'crepromatprocod',
        'creprofecemi',
        'creprofeccad',
        'creprotipo',
        'creprocarnet',
    )


@admin.register(CredencialPrograma)
class CredencialProgramaAdmin(admin.ModelAdmin):
    list_display = (
        'creproestcod',
        'creproprocod',
        'creprofecemi',
        'creprofeccad',
        'creprotipo',
        'creprocarnet',
    )



# Registro del modelo CertificadoCursoMatricula
@admin.register(CertificadoCursoMatriculado)
class CertificadoCursoMatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'cercurmatcurcod',
        'cercurfecemi',
        'cercurfeccad',
        'cercurcarnet',
    )


# Registro del modelo CertificadoCurso
@admin.register(CertificadoCurso)
class CertificadoCursoAdmin(admin.ModelAdmin):
    list_display = (
        'cercurestcod',
        'cercurcurcod',
        'cercurfecemi',
        'cercurfeccad',
        'cercurcarnet',
    )