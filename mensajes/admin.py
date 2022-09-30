from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Mensaje)
class AMensajeAdmin(ImportExportModelAdmin):
    pass

@admin.register(MensajeErrores)
class MensajeErroresAdmin(ImportExportModelAdmin):
    pass

@admin.register(CatalogosErrores)
class CatalogosErroresAdmin(ImportExportModelAdmin):
    pass

