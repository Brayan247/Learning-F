from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Plan)
class AdministradorAdmin(ImportExportModelAdmin):
    list_display = ('idplan', 'nombre', 'acronimo', 'descripcion', 'costo')
    pass

@admin.register(DetallePlan)
class AdministradorAdmin(ImportExportModelAdmin):
    list_display = ('plan_idplan', 'modulo_idmodulo')
    pass

@admin.register(PlanContrato)
class AdministradorAdmin(ImportExportModelAdmin):
    list_display = ('plan_idplan', 'contrato_idcontrato', 'contrato_entidad_identidad',)
    pass

