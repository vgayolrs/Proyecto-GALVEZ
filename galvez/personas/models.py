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
    def __str__(self):
        return self.nombre

class TipoOcupacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class TituloOcupacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    tipo_ocupacion = models.ForeignKey(TipoOcupacion, on_delete=models.CASCADE, null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Ocupacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    titulo_ocupacion = models.ForeignKey(TituloOcupacion, on_delete=models.CASCADE, null=True)
    fecha_inicio = models.IntegerField(null=True, blank=True)
    fecha_final = models.IntegerField(null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return '%s, %s' % (self.persona, self.titulo_ocupacion)
