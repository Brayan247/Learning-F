from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Perfil)
class PerfilAdmin(ImportExportModelAdmin):
    pass

@admin.register(PerfilAdministrador)
class PerfilAdministradorAdmin(ImportExportModelAdmin):
    pass


