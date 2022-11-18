from django.contrib import admin
from .models import *

from apps.administrador.utilities import *

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('idmodulo', 'modulo', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ModuloPerfilAdmin(admin.ModelAdmin):
    list_display = ('idmodulo', 'idperfil')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ModuloAdministradorAdmin(admin.ModelAdmin):
    list_display = ('idmodulo', 'idadministrador')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Modulo, ModuloAdmin)
admin.site.register(ModuloPerfil, ModuloPerfilAdmin)
admin.site.register(Moduloadministrador, ModuloAdministradorAdmin)