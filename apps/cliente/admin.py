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

class ClienteBotAdmin(admin.ModelAdmin):
    list_display = ('idcliente', 'nombres', 'apellidos')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
class ClienteBotHasEntidadAdmin(admin.ModelAdmin):
    list_display = ('cliente_bot_idcliente', 'entidad_identidad')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
    
admin.site.register(ClienteBot, ClienteBotAdmin)
admin.site.register(ClienteBotHasEntidad, ClienteBotHasEntidadAdmin)
