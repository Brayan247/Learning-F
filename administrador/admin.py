from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Administrador)
class AdministradorAdmin(ImportExportModelAdmin):
    list_display = ('idadministrador', 'usuario', 'nombres', 'apellidos')
    pass

@admin.register(UserEntidad)
class UserEntidadAdmin(ImportExportModelAdmin):
    list_display = ('id_user_entidad', 'id_user', 'id_entidad')
    pass