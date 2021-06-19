# personas/admin.py

from django.contrib import admin
from personas.models import Persona, TipoOcupacion, TituloOcupacion, TipoResidencia, Ocupacion, TipoRelacion, Relacion, Actividad
from actividades.models import Cargo, Asignacion

class CargoInline(admin.StackedInline):
    model = Cargo
    extra = 0
    ordering = ('titulo_cargo',)

class OcupacionInline(admin.StackedInline):
    model = Ocupacion
    extra = 0
    ordering = ('titulo_ocupacion',)

class AsignacionInline(admin.TabularInline):
    model = Asignacion
    extra = 0
    ordering = ('asignacion',)

class ActividadInline(admin.TabularInline):
    model = Actividad
    extra = 0
    ordering = ('fecha',)

class RelacionInline(admin.TabularInline):
    model = Relacion
    fk_name = "persona_id_1"
    extra = 0
    ordering = ('fecha_inicio',)

class PersonaAdmin(admin.ModelAdmin):
    fields = ('id', ('nombre', 'ordenar_por_nombre'), 'genero', 'fecha_nacimiento', 'lugar_nacimiento', 'fecha_defuncion', 'lugar_defuncion', 'notas')
    inlines = [OcupacionInline, CargoInline, AsignacionInline, ActividadInline, RelacionInline,]
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

class TipoRelacionAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TipoRelacion, TipoRelacionAdmin)

class   RelacionAdmin(admin.ModelAdmin):
    ordering = ('fecha_inicio',)
admin.site.register(Relacion, RelacionAdmin)
