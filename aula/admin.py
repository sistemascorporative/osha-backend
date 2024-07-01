from django.contrib import admin
from .models import *

# Register your models here.
    
admin.site.register(EstadoRegistro)


# Registro del modelo Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('curcod', 'curnom', 'curnummod', 'curestregcod')
    search_fields = ('curnom',)
    list_filter = ('curestregcod',)  # Puedes añadir filtros basados en los campos del modelo
    ordering = ('curnom',)  # Ordena por nombre del curso


# Registro del modelo Programa
@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('procod', 'pronom', 'procodosh', 'pronumcur', 'proestregcod')
    search_fields = ('pronom',)
    filter_horizontal = ('cursos',)  # Esto habilita la interfaz para gestionar la relación muchos a muchos
    list_filter = ('proestregcod',)  # Añade filtros basados en los campos del modelo
    ordering = ('pronom',)  # Ordena por nombre del programa


@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('modcod', 'modnom', 'modcurcod', 'modestregcod')
    search_fields = ('modnom',)
    list_filter = ('modestregcod',)
    ordering = ('modcod',)


admin.site.register(Examen)
admin.site.register(Pregunta)
admin.site.register(Alternativa)
admin.site.register(Respuesta)
admin.site.register(Matricula)
admin.site.register(RegistroCurso)
admin.site.register(RegistroExamen)
admin.site.register(NotaPrograma)