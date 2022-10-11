from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Perfil)
class PerfilAdmin(ImportExportModelAdmin):
    list_display = ('idperfil', 'perfil', 'descripcion')
    pass

@admin.register(PerfilAdministrador)
class PerfilAdministradorAdmin(ImportExportModelAdmin):
    list_display = ('idadministrador', 'idperfil')
    pass


