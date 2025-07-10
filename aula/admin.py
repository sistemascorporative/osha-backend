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
    search_fields = ('estexanom',)


# Registro del modelo Matricula Programa
@admin.register(MatriculaPrograma)
class MatriculaProgramaAdmin(admin.ModelAdmin):
    list_display = (
        'matproestcod',
        'matproter',
        'matpropun',
        'matprofecini',
        'matprofecfin',
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
    list_filter = ('curfre', 'curestregcod')
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
    search_fields = ('procod','pronom','procodosh',)
    filter_horizontal = ('cursos',)
    list_filter = ('proestregcod',)
    ordering = ('procod',)


# Registro del modelo Modulo
@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = (
        'modcod',
        'modnom',
        'modcurcod',
        'modestregcod'
    )
    search_fields = ('modcod','modnom',)
    list_filter = ('modestregcod','modcurcod',)


# Registro del modelo Examen
@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    list_display = (
        'exacurcod',
        'exanumpre',
        'exaestregcod',
    )
    search_fields = ('exacurcod',)
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
    search_fields = ('precod','pretex',)
    list_filter = ('preestregcod','preexacod')


# Registro del modelo Alternativa
@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    list_display = (
        'altcod',
        'altcor',
        'alttex',
        'altprecod',
        'altestregcod',
    )
    search_fields = ('alttex', 'altcod')
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
    )
    search_fields = ('resproestcod','resproprocod','resproexacod','resproprecod',)
    list_filter = ('resproexacod',)


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
    )
    search_fields = ('rescurestcod','rescurexacod','rescurprecod',)
    list_filter = ('rescurexacod',)


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
    search_fields = ('regexaproprocod','regexaproestcod','regexaproexacod',)
    list_filter = ('regexaproprocod',)


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
    search_fields = ('regexacurcurcod','regexacurestcod','regexacurexacod',)
    list_filter = ('regexacurcurcod',)