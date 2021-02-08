from tareas.models import Tarea
from rest_framework import serializers


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        '''fields = ['descripcion', 'duracion', 'tiempo_registrado', 'estatus']'''
        fields= '__all__'