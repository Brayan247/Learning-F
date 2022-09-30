from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Plan)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(DetallePlan)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(PlanContrato)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

