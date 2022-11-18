from django.contrib import admin
from .models import *

from apps.administrador.utilities import *

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('idperfil', 'perfil', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class PerfilAdministradorAdmin(admin.ModelAdmin):
    list_display = ('idadministrador', 'idperfil')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(PerfilAdministrador, PerfilAdministradorAdmin)