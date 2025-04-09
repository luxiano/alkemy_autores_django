from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo', 'fecha_creacion', 'fecha_modificacion')
    list_filter = ('nacionalidad', 'activo')
    search_fields = ('nombre',)
    ordering = ('nombre',)