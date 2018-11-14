# personas/models.py

from django.db import models

# Create your models here.

class Persona(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    genero = models.CharField(max_length=765, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    fecha_defuncion = models.DateField(null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self)
        return self.nombre
