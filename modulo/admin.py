from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Modulo)
class ModuloAdmin(ImportExportModelAdmin):
    list_display = ('idmodulo', 'modulo', 'descripcion')
    pass

@admin.register(ModuloPerfil)
class ModuloPerfilAdmin(ImportExportModelAdmin):
    list_display = ('idmodulo', 'idperfil')
    pass

@admin.register(Moduloadministrador)
class ModuloAdministradorAdmin(ImportExportModelAdmin):
    list_display = ('idmodulo', 'idadministrador')
    pass

