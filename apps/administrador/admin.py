#
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

class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('idadministrador', 'usuario', 'nombres', 'apellidos')
    actions = [acticacion_Logica, eliminacion_Logica]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class UserEntidadAdmin(admin.ModelAdmin):
    list_display = ('id_user_entidad', 'id_user', 'id_entidad')
    actions = [acticacion_Logica, eliminacion_Logica]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(UserEntidad, UserEntidadAdmin)
