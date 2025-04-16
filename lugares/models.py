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

class TipoLocalidad(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Localidad(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    tipo_localidad = models.ForeignKey(TipoLocalidad, on_delete=models.CASCADE, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    notas = models.TextField(blank=True)
    sistema_coordenadas = models.ForeignKey(SistemaCoordenadas, on_delete=models.CASCADE, null=True,  blank=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return  self.nombre

class Jurisdiccion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre

class EnJurisdiccion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE, null=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return '%s, %s' % (self.localidad, self.jurisdiccion)

class Provincia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre

class EnProvincia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True)
    fecha_inicio = models.IntegerField(null=True, blank=True)
    fecha_final = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return '%s en %s' % (self.jurisdiccion, self.provincia)

class Audiencia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    class Meta:
        ordering = ["nombre"]
    def __str__(self):
        return self.nombre

class EnAudiencia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE, null=True)
    audiencia = models.ForeignKey(Audiencia, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return '%s en %s' % (self.jurisdiccion, self.audiencia)
