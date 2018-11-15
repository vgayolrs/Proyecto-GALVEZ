# personas/admin.py

from django.contrib import admin

# Register your models here.

from personas.models import Persona, TipoOcupacion, TituloOcupacion, Ocupacion

class OcupacionInline(admin.StackedInline):
    model = Ocupacion
    extra = 0
    ordering = ('titulo_ocupacion',)

class PersonaAdmin(admin.ModelAdmin):
    fields = ('id', 'nombre', 'genero', 'fecha_nacimiento', 'fecha_defuncion', 'notas')
    inlines = [OcupacionInline]
    search_fields = ['nombre', 'genero', 'notas']
    list_display = ('nombre',)
    readonly_fields = ['id']
admin.site.register(Persona, PersonaAdmin)

class TipoOcupacionAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TipoOcupacion, TipoOcupacionAdmin)

class TituloOcupacionAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TituloOcupacion, TituloOcupacionAdmin)
