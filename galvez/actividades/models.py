# actividades/model.py

from django.db import models
from personas.models import Persona
from lugares.models import Localidad, Jurisdiccion, Provincia

class TipoCargo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class TituloCargo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE, null=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Cargo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    titulo_cargo = models.ForeignKey(TituloCargo, on_delete=models.CASCADE, null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True, blank=True)
    jurisdiccion = models.ForeignKey(Jurisdiccion, on_delete=models.CASCADE, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inicio = models.IntegerField(null=True, blank=True)
    fecha_final = models.IntegerField(null=True, blank=True)
    notas = models.TextField(blank=True)
    class Meta:
        ordering = ["fecha_inicio", "fecha_final"]
    def __str__(self):
        return "%s | %s | %s | %s | %s | %d | %d" % (self.persona, self.titulo_cargo, self.localidad, self.jurisdiccion, self.provincia, self.fecha_inicio, self.fecha_final)

class TipoInstitucion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Institucion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    fecha_inicio = models.IntegerField(null=True, blank=True)
    fecha_final = models.IntegerField(null=True, blank=True)
    tipo_institucion = models.ForeignKey(TipoInstitucion, on_delete=models.CASCADE, null=True, blank=True)
    localidad_sede = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class TipoAsignacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class TituloAsignacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    tipo_asignacion = models.ForeignKey(TipoAsignacion, on_delete=models.CASCADE, null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, null=True, blank=True)
    asignacion = models.ForeignKey(TituloAsignacion, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inicio = models.IntegerField(null=True, blank=True)
    fecha_final = models.IntegerField(null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return "%s | %s | %s | %d | %d" % (self.persona, self.institucion, self.asignacion, self.fecha_inicio, self.fecha_final)
