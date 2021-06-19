# personas/models.py

from django.db import models
from lugares.models import Localidad

class Persona(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    ordenar_por_nombre = models.CharField(max_length=100, blank=True)
    genero = models.CharField(max_length=765, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    lugar_nacimiento = models.ForeignKey(Localidad, related_name='nacimiento', on_delete=models.CASCADE, null=True, blank=True)
    fecha_defuncion = models.DateField(null=True, blank=True)
    lugar_defuncion = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class TipoResidencia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    temporal = models.NullBooleanField(null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Residencia(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, null=True)
    tipo_residencia = models.ForeignKey(TipoResidencia, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inicio = models.IntegerField(null=True, blank=True)
    fecha_final = models.IntegerField(null=True, blank=True)
    lugar_nacimiento = models.NullBooleanField(null=True, blank=True)
    lugar_defuncion = models.NullBooleanField(null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return '%s, %s' % (self.persona, self.tipo_residencia)

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

class TipoRelacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=765)
    notas = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Relacion(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona_id_1 = models.ForeignKey(Persona, related_name='persona_1', on_delete=models.CASCADE, null=True)
    persona_id_2 = models.ForeignKey(Persona, related_name='persona_2', on_delete=models.CASCADE, null=True)
    tipo_relacion = models.ForeignKey(TipoRelacion, on_delete=models.CASCADE, null=True)
    fecha_inicio = models.IntegerField(null=True, blank=True)
    fecha_final = models.IntegerField(null=True, blank=True)
    notas = models.TextField(blank=True)
    def __str__(self):
        return '%s and %s' % (self.persona_id_1, self.persona_id_2)

class Actividad(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)
    fecha = models.IntegerField(null=True, )
    actividad = models.TextField(blank=True)
    fuente = models.CharField(max_length=765, blank=True)
    def __str__(self):
        return self.actividad
