from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Pais)
class PaisAdmin(ImportExportModelAdmin):
    pass

@admin.register(Moneda)
class MonedaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Ciudad)
class CuidadAdmin(ImportExportModelAdmin):
    pass
