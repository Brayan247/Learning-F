from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class MensajeAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idmensaje','mensaje', 'eliminado')

class MensajeErroresAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idmensaje_error','mensaje', 'id_entidad', 'eliminado')

class CatalogosErroresAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idmsg_error','nombre', 'eliminado')

admin.site.register(Mensaje, MensajeAdmin)
admin.site.register(MensajeErrores, MensajeErroresAdmin)
admin.site.register(CatalogosErrores, CatalogosErroresAdmin)