from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(CamposPersonalizadosNuevaCuenta)
class CamposPersonalizadosNuevaCuentaAdmin(ImportExportModelAdmin):
    list_display = ('idcampo', 'nombre', 'placeholder', 'identificador')
    pass

@admin.register(CamposPersonalizadosEntidad)
class CamposPersonalizadosEntidadAdmin(ImportExportModelAdmin):
    list_display = ('entidad_identidad', 'campos_personalizados_nueva_cuenta_idcampo')
    pass

@admin.register(TiposCampos)
class TiposCamposAdmin(ImportExportModelAdmin):
    list_display = ('idtipo', 'nombre', 'descripcion')
    pass

@admin.register(OpcionesCampo)
class OpcionesCampoAdmin(ImportExportModelAdmin):
    list_display = ('idopcion', 'valor', 'nombre')
    pass
