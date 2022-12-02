from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class ModuloAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idmodulo', 'modulo', 'eliminado')

class ModuloPerfilAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idmodulo', 'idperfil', 'eliminado')

class ModuloAdministradorAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idmodulo', 'idadministrador', 'eliminado')

admin.site.register(Modulo, ModuloAdmin)
admin.site.register(ModuloPerfil, ModuloPerfilAdmin)
admin.site.register(Moduloadministrador, ModuloAdministradorAdmin)