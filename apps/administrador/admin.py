#
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class AdministradorAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idadministrador', 'usuario', 'eliminado')

class UserEntidadAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_user_entidad', 'id_user', 'id_entidad', 'eliminado')


admin.site.register(Administrador, AdministradorAdmin)
admin.site.register(UserEntidad, UserEntidadAdmin)
