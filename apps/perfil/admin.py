from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class PerfilAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idperfil', 'perfil', 'eliminado')

class PerfilAdministradorAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idadministrador', 'idperfil', 'eliminado')

admin.site.register(Perfil, PerfilAdmin)
admin.site.register(PerfilAdministrador, PerfilAdministradorAdmin)