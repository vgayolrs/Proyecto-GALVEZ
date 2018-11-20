#lugares/admin.py

from django.contrib import admin

# Register your models here.

from lugares.models import Localidad, SistemaCoordenadas, EnTerritorio, Territorio

class EnTerritorioInline(admin.TabularInline):
    model = EnTerritorio
    extra = 0

class LocalidadAdmin(admin.ModelAdmin):
    fields = ('nombre', ('lat', 'long', 'sistema_coordenadas'), 'notas')
    inlines = [EnTerritorioInline]
    search_fields = ['nombre', 'notas']
admin.site.register(Localidad, LocalidadAdmin)

class SistemaCoordenadasAdmin(admin.ModelAdmin):
    pass
admin.site.register(SistemaCoordenadas, SistemaCoordenadasAdmin)

class TerritorioAdmin(admin.ModelAdmin):
    inlines = [EnTerritorioInline]
admin.site.register(Territorio, TerritorioAdmin)
