from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class PaisAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idpais', 'pais', 'eliminado')

class MonedaAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_moneda', 'moneda', 'simbolo', 'eliminado')

class CiudadAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idciudad', 'ciudad', 'eliminado')

admin.site.register(Pais, PaisAdmin)
admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Ciudad, CiudadAdmin)