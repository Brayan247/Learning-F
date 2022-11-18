from django.contrib import admin
from .models import *

from apps.administrador.utilities import *

class CamposPersonalizadosNuevaCuentaAdmin(admin.ModelAdmin):
    list_display = ('idcampo', 'nombre', 'placeholder', 'identificador')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class CamposPersonalizadosEntidadAdmin(admin.ModelAdmin):
    list_display = ('entidad_identidad', 'campos_personalizados_nueva_cuenta_idcampo')
    actions = [acticacion_Logica, eliminacion_Logica]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class TiposCamposAdmin(admin.ModelAdmin):
    list_display = ('idtipo', 'nombre', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class OpcionesCampoAdmin(admin.ModelAdmin):
    list_display = ('idopcion', 'valor', 'nombre')
    actions = [acticacion_Logica, eliminacion_Logica]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

admin.site.register(CamposPersonalizadosNuevaCuenta, CamposPersonalizadosNuevaCuentaAdmin)
admin.site.register(CamposPersonalizadosEntidad, CamposPersonalizadosEntidadAdmin)
admin.site.register(TiposCampos, TiposCamposAdmin)
admin.site.register(OpcionesCampo, OpcionesCampoAdmin)