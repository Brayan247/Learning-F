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

class MensajeAdmin(admin.ModelAdmin):
    list_display = ('idmensaje','mensaje', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class MensajeErroresAdmin(admin.ModelAdmin):
    list_display = ('idmensaje_error','mensaje', 'id_entidad')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class CatalogosErroresAdmin(admin.ModelAdmin):
    list_display = ('idmsg_error','nombre')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(MensajeErrores, MensajeErroresAdmin)
admin.site.register(CatalogosErrores, CatalogosErroresAdmin)