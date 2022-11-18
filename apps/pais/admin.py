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

class PaisAdmin(admin.ModelAdmin):
    list_display = ('idpais', 'pais', 'acronimo', 'codigoarea')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class MonedaAdmin(admin.ModelAdmin):
    list_display = ('id_moneda', 'moneda', 'simbolo', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('idciudad', 'ciudad', 'acronimo', 'comentario')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Pais, PaisAdmin)
admin.site.register(Moneda, MonedaAdmin)
admin.site.register(Ciudad, CiudadAdmin)