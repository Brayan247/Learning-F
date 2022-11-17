from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(ClienteBot)
class ClienteBotAdmin(ImportExportModelAdmin):
    list_display = ('idcliente', 'nombres', 'apellidos')
    pass

@admin.register(ClienteBotHasEntidad)
class ClienteBotHasEntidadAdmin(ImportExportModelAdmin):
    list_display = ('cliente_bot_idcliente', 'entidad_identidad')
    pass

