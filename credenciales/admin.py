from django.contrib import admin
from .models import *

# Register your models here.

# Registro del modelo Credencial
@admin.register(Credencial)
class CredencialAdmin(admin.ModelAdmin):
    list_display = (
        'crecod',
        'creestcod',
        'creprocod',
    )


# Registro del modelo Certificado
@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = (
        'cercod',
        'cerfecemi',
        'cerfeccad',
        'cersrc',
        'cercrecod',
        'cerestregcod',
    )


# Registro del modelo Diploma
@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    list_display = (
        'dipcod',
        'dipfecemi',
        'dipfeccad',
        'dipsrc',
        'dipcrecod',
        'dipestregcod',
    )


# Registro del modelo Carnet
@admin.register(Carnet)
class CarnetAdmin(admin.ModelAdmin):
    list_display = (
        'carcod',
        'carsrc',
        'carcrecod',
        'carestregcod',
    )