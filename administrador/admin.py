from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from django.contrib import admin
from .models import *


@admin.register(Administrador)
class AdministradorAdmin(ImportExportModelAdmin):
    pass


@admin.register(LogsSystemFintech)
class LogsSystemFintechAdmin(ImportExportModelAdmin):
    pass