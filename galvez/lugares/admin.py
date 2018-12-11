#lugares/admin.py

from django.contrib import admin

# Register your models here.

from lugares.models import Localidad, TipoLocalidad, SistemaCoordenadas, EnJurisdiccion, Jurisdiccion, EnProvincia, Provincia, EnAudiencia, Audiencia

class EnJurisdiccionInline(admin.TabularInline):
    model = EnJurisdiccion
    extra = 0

class EnProvinciaInline(admin.TabularInline):
    model = EnProvincia
    extra = 0

class EnAudienciaInline(admin.TabularInline):
    model = EnAudiencia
    extra = 0

class LocalidadAdmin(admin.ModelAdmin):
    fields = ('id', 'nombre', 'tipo_localidad', ( 'lat', 'long', 'sistema_coordenadas'), 'notas')
    inlines = [EnJurisdiccionInline]
    search_fields = ['nombre', 'notas']
    readonly_fields = ['id']
    ordering = ('nombre',)
admin.site.register(Localidad, LocalidadAdmin)

class SistemaCoordenadasAdmin(admin.ModelAdmin):
    pass
admin.site.register(SistemaCoordenadas, SistemaCoordenadasAdmin)

class TipoLocalidadAdmin(admin.ModelAdmin):
    pass
admin.site.register(TipoLocalidad, TipoLocalidadAdmin)

class JurisdiccionAdmin(admin.ModelAdmin):
    inlines = [EnProvinciaInline, EnAudienciaInline]
    search_fields = ['nombre']
    ordering = ('nombre',)
admin.site.register(Jurisdiccion, JurisdiccionAdmin)

class ProvinciaAdmin(admin.ModelAdmin):
    inlines = [EnProvinciaInline]
    ordering = ('nombre',)
admin.site.register(Provincia, ProvinciaAdmin)

class AudienciaAdmin(admin.ModelAdmin):
    inlines = [EnAudienciaInline]
    ordering = ('nombre',)
admin.site.register(Audiencia, AudienciaAdmin)
