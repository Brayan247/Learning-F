from django.contrib import admin
from .models import *

def acticacion_Logica(self, request, queryset):
    for object in queryset:
        object.eliminado = 0
        object.save()

def eliminacion_Logica(self, request, queryset):
    for object in queryset:
        object.eliminado = 1
        object.save()

class PlanAdmin(admin.ModelAdmin):
    list_display = ('idplan', 'nombre', 'acronimo', 'descripcion', 'costo')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class DetallePlanAdmin(admin.ModelAdmin):
    list_display = ('plan_idplan', 'modulo_idmodulo')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class PlanContratosAdmin(admin.ModelAdmin):
    list_display = ('plan_idplan', 'contrato_idcontrato', 'contrato_entidad_identidad',)
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Plan, PlanAdmin)
admin.site.register(DetallePlan, DetallePlanAdmin)
admin.site.register(PlanContrato, PlanContratosAdmin)