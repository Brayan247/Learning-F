from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Mensaje)
class AMensajeAdmin(ImportExportModelAdmin):
    list_display = ('idmensaje','mensaje', 'descripcion')
    pass

@admin.register(MensajeErrores)
class MensajeErroresAdmin(ImportExportModelAdmin):
    list_display = ('idmensaje_error','mensaje')
    pass

@admin.register(CatalogosErrores)
class CatalogosErroresAdmin(ImportExportModelAdmin):
    list_display = ('idmsg_error','nombre')
    pass

