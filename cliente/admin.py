from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(ClienteBot)
class ClienteBotAdmin(ImportExportModelAdmin):
    pass

@admin.register(ClienteBotHasEntidad)
class ClienteBotHasEntidadAdmin(ImportExportModelAdmin):
    pass

