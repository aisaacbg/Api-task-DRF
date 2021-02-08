from django.db import models
from django.utils import timezone

status = (
    ('pendiente', 'Tarea pendiente'),
    ('completada', 'Tarea completada')
)

# Create your models here.
class Tarea(models.Model):
    descripcion=models.CharField(max_length=40)
    duracion=models.IntegerField()
    tiempo_registrado=models.DateTimeField(blank=True,null=True)
    estatus=models.CharField(max_length=15, choices=status)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='tarea'