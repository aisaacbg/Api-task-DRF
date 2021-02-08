from django.contrib import admin
from tareas.models import Tarea
# Register your models here.


class TareasAdmin(admin.ModelAdmin):
    list_display=("descripcion", "duracion", "tiempo_registrado", "estatus" )


admin.site.register(Tarea, TareasAdmin)