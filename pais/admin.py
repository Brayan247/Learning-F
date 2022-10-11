from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Pais)
class PaisAdmin(ImportExportModelAdmin):
    list_display = ('idpais', 'pais', 'acronimo', 'codigoarea')
    pass

@admin.register(Moneda)
class MonedaAdmin(ImportExportModelAdmin):
    list_display = ('id_moneda', 'moneda', 'simbolo', 'descripcion')
    pass

@admin.register(Ciudad)
class CuidadAdmin(ImportExportModelAdmin):
    list_display = ('idciudad', 'ciudad', 'acronimo', 'comentario')
    pass
