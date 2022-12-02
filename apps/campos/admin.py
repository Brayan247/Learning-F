from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class CamposPersonalizadosNuevaCuentaAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idcampo', 'nombre', 'eliminado')

class CamposPersonalizadosEntidadAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('entidad_identidad', 'campos_personalizados_nueva_cuenta_idcampo', 'eliminado')

class TiposCamposAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idtipo', 'nombre', 'eliminado')

class OpcionesCampoAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idopcion', 'valor', 'nombre', 'eliminado')

admin.site.register(CamposPersonalizadosNuevaCuenta, CamposPersonalizadosNuevaCuentaAdmin)
admin.site.register(CamposPersonalizadosEntidad, CamposPersonalizadosEntidadAdmin)
admin.site.register(TiposCampos, TiposCamposAdmin)
admin.site.register(OpcionesCampo, OpcionesCampoAdmin)