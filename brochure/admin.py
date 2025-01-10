from django.contrib import admin
from .models import *


@admin.register(Brochure)
class BrochureAdmin(admin.ModelAdmin):
    list_display = (
        'broprocod',
        'bronummod',
    )


@admin.register(BModulo)
class BModuloAdmin(admin.ModelAdmin):
    list_display = (
        'bmodnomes',
        'bmodnomen',
        'bmodbrocod',
    )

