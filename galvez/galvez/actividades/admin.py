# actividades/admin.py
from django.contrib import admin
from actividades.models import Cargo, TituloCargo, TipoCargo

class CargoAdmin(admin.ModelAdmin):
    fields = ('id', 'persona', 'titulo_cargo', 'localidad', ('fecha_inicio', 'fecha_final'), 'notas' )
    search_fields = ['persona__nombre', 'titulo_cargo__nombre', 'localidad__nombre', 'notas']
    list_display = ('persona', 'titulo_cargo', 'localidad', 'fecha_inicio', 'fecha_final')
    readonly_fields = ['id']
    ordering = ('fecha_inicio', 'fecha_final',)
admin.site.register(Cargo, CargoAdmin)

class TituloCargoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'notas']
    readonly_fields = ['id']
    list_display = ('nombre', 'tipo_cargo')
    ordering = ('nombre',)
admin.site.register(TituloCargo, TituloCargoAdmin)

class TipoCargoAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TipoCargo)
