from django.contrib import admin
from .models import *

# Register your models here.

# Registro del modelo EStudiante usuario personalizado
@admin.register(EstudianteUser)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'usernom',
        'userape',
        'is_staff',
        'is_active',
        'userdocide',
    )
    search_fields = ('usernom', 'userape', 'userdocide', 'usercodosh',)
    list_filter = ('is_staff','userpai',)