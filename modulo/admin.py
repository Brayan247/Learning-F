from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Modulo)
class ModuloAdmin(ImportExportModelAdmin):
    pass

@admin.register(ModuloPerfil)
class ModuloPerfilAdmin(ImportExportModelAdmin):
    pass

@admin.register(Moduloadministrador)
class ModuloAdministradorAdmin(ImportExportModelAdmin):
    pass

