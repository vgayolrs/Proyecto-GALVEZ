#lugares/models.py

from django.db import models

# Los modelos de tablas de la BD y sus relaciones.

class SistemaCoordenadas(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre_corto = models.CharField(max_length=150)
    nombre_largo = models.CharField(max_length=765, blank=True)
    notas = models.TextField(blank=True)
    referencia = models.CharField(max_length=765, blank=True)
    def __str__(self):
        return self.nombre_corto

class Localidad(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    notas = models.TextField(blank=True)
    sistema_coordenadas = models.ForeignKey(SistemaCoordenadas, on_delete=models.CASCADE, null=True,  blank=True)
    def __str__(self):
        return  self.nombre

class Territorio(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class EnTerritorio(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True)
    territorio = models.ForeignKey(Territorio, on_delete=models.CASCADE, null=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return '%s, %s' % (self.localidad, self.territorio)

