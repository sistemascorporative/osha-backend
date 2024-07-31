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


# Registro del modelo Estado de Registro
@admin.register(EstadoExamen)
class EstadoExamenAdmin(admin.ModelAdmin):
    list_display = (
        'estexacod',
        'estexanom'
    )


# Registro del modelo EStudiante usuario personalizado
@admin.register(EstudianteUser)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'estusernom',
        'estuserape',
        'estuserdocide',
        'is_active',
        'is_staff',
        'is_superuser'
    )
    search_fields = ('estusernom', 'estuserape','email','estuserdocide',)


# Registro del modelo Matricula
@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = (
        'matcod',
        'matestcod',
        'matprocod',
        'matestregcod'
    )
    search_fields = ('matcod',)
    list_filter = ('matprocod',)


# Registro del modelo Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'curcod',
        'curnom',
        'curnummod',
        'curestregcod'
    )
    search_fields = ('curcod', 'curnom')
    list_filter = ('curestregcod',)
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
    search_fields = ('pronom',)
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
        'exacod',
        'exanumpre',
        'exacurcod',
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


# Registro del modelo Respuesta
admin.site.register(Respuesta)


# Registro del modelo Pregunta
admin.site.register(RegistroCurso)


# Registro del modelo Pregunta
@admin.register(RegistroExamen)
class RegistroExamenAdmin(admin.ModelAdmin):
    list_display = (
        'regexacod',
        'regexapun',
        'regexaint',
        'regexaestexacod',
        'regexaestprocod',
        'regexaestcod',
        'regexaexacod',
    )


# Registro del modelo Pregunta
@admin.register(NotaPrograma)
class NotaProgramaAdmin(admin.ModelAdmin):
    list_display = (
        'notprocod',
        'notpropun',
        'notproestcod',
        'notproprocod',
    )

