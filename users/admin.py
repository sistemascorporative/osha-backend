from django.contrib import admin
from .models import *

# Register your models here.

# Registro del modelo UserSimple personalizado
@admin.register(UserSimple)
class UserSimpleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'userdocide',
        'usercodosh',
        'usernom',
        'userape',
        'userpai',
    )
    search_fields = ('id', 'usernom', 'userape', 'userdocide', 'usercodosh',)
    list_filter = ('userpai',)


# Registro del modelo EStudiante usuario personalizado
@admin.register(EstudianteUser)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'is_staff',
        'is_active',
    )
    search_fields = ('email',)
    list_filter = ('is_staff',)