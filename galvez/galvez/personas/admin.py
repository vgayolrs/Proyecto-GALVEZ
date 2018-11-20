# personas/admin.py

from django.contrib import admin
from personas.models import Persona, TipoOcupacion, TituloOcupacion, TipoResidencia, Ocupacion
from actividades.models import Cargo

class CargoInline(admin.StackedInline):
    model = Cargo
    extra = 0
    ordering = ('titulo_cargo',)

class OcupacionInline(admin.StackedInline):
    model = Ocupacion
    extra = 0
    ordering = ('titulo_ocupacion',)

class PersonaAdmin(admin.ModelAdmin):
    fields = ('id', ('nombre', 'ordenar_por_nombre'), 'genero', 'fecha_nacimiento', 'fecha_defuncion', 'notas')
    inlines = [OcupacionInline, CargoInline]
    search_fields = ['nombre', 'genero', 'notas']
    list_display = ('nombre',)
    readonly_fields = ['id']
    ordering = ('ordenar_por_nombre',)
admin.site.register(Persona, PersonaAdmin)

class TipoOcupacionAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TipoOcupacion, TipoOcupacionAdmin)

class TituloOcupacionAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TituloOcupacion, TituloOcupacionAdmin)

class TipoResidenciaAdmin(admin.ModelAdmin):
    pass
admin.site.register(TipoResidencia, TipoResidenciaAdmin)
