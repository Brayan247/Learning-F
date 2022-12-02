from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class PlanAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idplan', 'nombre', 'eliminado')
    
class DetallePlanAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('plan_idplan', 'modulo_idmodulo', 'eliminado')
    
class PlanContratosAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('plan_idplan', 'contrato_idcontrato', 'contrato_entidad_identidad', 'eliminado')

admin.site.register(Plan, PlanAdmin)
admin.site.register(DetallePlan, DetallePlanAdmin)
admin.site.register(PlanContrato, PlanContratosAdmin)