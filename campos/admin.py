from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(CamposPersonalizadosNuevaCuenta)
class CamposPersonalizadosNuevaCuentaAdmin(ImportExportModelAdmin):
    pass

@admin.register(TiposCampos)
class TiposCamposAdmin(ImportExportModelAdmin):
    pass

@admin.register(OpcionesCampo)
class OpcionesCampoAdmin(ImportExportModelAdmin):
    pass
