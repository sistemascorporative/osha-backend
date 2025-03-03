from django.contrib import admin
from .models import *

# Register your models here.


# Registro del modelo Estado de Registro
@admin.register(EstadoRegistro)
class EstadoRegistroAdmin(admin.ModelAdmin):
    list_display = (
        'estregcod',
        'estregnom'
    )


# Registro del modelo Estado de Examen
@admin.register(EstadoExamen)
class EstadoExamenAdmin(admin.ModelAdmin):
    list_display = (
        'estexacod',
        'estexanom'
    )


# Registro del modelo Matricula Programa
@admin.register(MatriculaPrograma)
class MatriculaProgramaAdmin(admin.ModelAdmin):
    list_display = (
        'matprocod',
        'matprofecini',
        'matprofecfin',
        'matproter',
        'matproestcod',
        'matproprocod',
        'matproestregcod'
    )
    search_fields = ('matproestcod', 'matproprocod',)
    list_filter = ('matproprocod',)


# Registro del modelo Matricula Curso
@admin.register(MatriculaCurso)
class MatriculaCursoAdmin(admin.ModelAdmin):
    list_display = (
        'matcurcod',
        'matcurfecini',
        'matcurfecfin',
        'matcurestcod',
        'matcurcurcod',
        'matcurestregcod'
    )
    search_fields = ('matcurestcod', 'matcurcurcod',)
    list_filter = ('matcurcurcod',)


# Registro del modelo Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'curcod',
        'curnom',
        'curnummod',
        'curfre',
        'curestregcod'
    )
    search_fields = ('curcod', 'curnom')
    list_filter = ('curfre',)
    ordering = ('curcod',)


# Registro del modelo Programa
@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = (
        'procod',
        'pronom',
        'procodosh',
        'pronumcur',
        'pronumhor',
        'proestregcod'
    )
    search_fields = ('pronom','procodosh',)
    filter_horizontal = ('cursos',)
    list_filter = ('proestregcod',)
    ordering = ('pronom',)


# Registro del modelo Modulo
@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = (
        'modcod',
        'modnom',
        'modcurcod',
        'modestregcod'
    )
    search_fields = ('modnom',)
    list_filter = ('modestregcod','modcurcod',)


# Registro del modelo Examen
@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = (
        'exacurcod',
        'exanumpre',
        'exaestregcod',
    )
    list_filter = ('exaestregcod',)


# Registro del modelo Pregunta
@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = (
        'precod',
        'pretex',
        'preexacod',
        'preestregcod',
    )
    search_fields = ('pretex',)
    list_filter = ('preestregcod',)


# Registro del modelo Alternativa
@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    list_display = (
        'altcod',
        'alttex',
        'altcor',
        'altprecod',
        'altestregcod',
    )
    search_fields = ('alttex',)
    list_filter = ('altestregcod',)


# Registro del modelo RespuestaExamenPrograma
@admin.register(RespuestaExamenPrograma)
class RespuestaExamenProgramaAdmin(admin.ModelAdmin):
    list_display = (
        'resprocod',
        'respropun',
        'resproestcod',
        'resproprocod',
        'resproexacod',
        'resproprecod',
        'resproaltcod',
        'resprofec',
    )


# Registro del modelo RespuestaExamenCurso
@admin.register(RespuestaExamenCurso)
class RespuestaExamenCursoAdmin(admin.ModelAdmin):
    list_display = (
        'rescurcod',
        'rescurpun',
        'rescurestcod',
        'rescurexacod',
        'rescurprecod',
        'rescuraltcod',
        'rescurfec',
    )


@admin.register(RegistroExamenPrograma)
class RegistroExamenProgramaAdmin(admin.ModelAdmin):
    list_display = (
        'regexaprocod',
        'regexapropun',
        'regexaproint',
        'regexaproprocod',
        'regexaproestcod',
        'regexaproexacod',
        'regexaproestexacod',
    )


@admin.register(RegistroExamenCurso)
class RegistroExamenCursoAdmin(admin.ModelAdmin):
    list_display = (
        'regexacurcod',
        'regexacurpun',
        'regexacurint',
        'regexacurcurcod',
        'regexacurestcod',
        'regexacurexacod',
        'regexacurestexacod',
    )


