from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class ClienteBotAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idcliente', 'nombres', 'apellidos', 'eliminado')
    
class ClienteBotHasEntidadAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cliente_bot_idcliente', 'entidad_identidad', 'eliminado')

admin.site.register(ClienteBot, ClienteBotAdmin)
admin.site.register(ClienteBotHasEntidad, ClienteBotHasEntidadAdmin)
