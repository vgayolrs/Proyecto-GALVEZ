# actividades/admin.py
from django.contrib import admin
from actividades.models import Cargo, TituloCargo, TipoCargo, Asignacion, TituloAsignacion, TipoAsignacion, Institucion, TipoInstitucion

class CargoAdmin(admin.ModelAdmin):
    fields = ('id', 'persona', 'titulo_cargo', 'localidad', 'jurisdiccion', 'provincia', ('fecha_inicio', 'fecha_final'), 'notas' )
    search_fields = ['persona__nombre', 'titulo_cargo__nombre', 'localidad__nombre', 'jurisdiccion__nombre', 'provincia__nombre', 'notas']
    list_display = ('persona', 'titulo_cargo', 'localidad', 'jurisdiccion', 'fecha_inicio', 'fecha_final')
    readonly_fields = ['id']
    ordering = ('fecha_inicio', 'fecha_final',)
admin.site.register(Cargo, CargoAdmin)

class AsignacionAdmin(admin.ModelAdmin):
    fields = ('id', 'persona', 'institucion', 'asignacion', ('fecha_inicio', 'fecha_final'), 'notas')
    search_fields = ['persona__nombre', 'institucion__nombre', 'asignacion__nombre']
    readonly_fields = ['id']
admin.site.register(Asignacion, AsignacionAdmin)

class InstitucionAdmin(admin.ModelAdmin):
    fields = ('id', 'nombre', 'tipo_institucion', ('fecha_inicio', 'fecha_final'), 'notas')
    search_fields = ['institucion__nombre']
    readonly_fields = ['id']
admin.site.register(Institucion, InstitucionAdmin)

class TituloCargoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'notas']
    readonly_fields = ['id']
    list_display = ('nombre', 'tipo_cargo')
    ordering = ('nombre',)
admin.site.register(TituloCargo, TituloCargoAdmin)

class TipoCargoAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TipoCargo)

class TituloAsignacionAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'notas']
    readonly_fields = ['id']
    list_display = ('nombre', 'tipo_asignacion')
    ordering = ('nombre',)
admin.site.register(TituloAsignacion, TituloAsignacionAdmin)

class TipoAsignacionAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TipoAsignacion)

class TipoInstitucionAdmin(admin.ModelAdmin):
    ordering = ('nombre',)
admin.site.register(TipoInstitucion)
