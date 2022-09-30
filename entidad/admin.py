from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Entidad)
class EntidadAdmin(ImportExportModelAdmin):
    pass

@admin.register(CamposPersonalizadosEntidad)
class CamposPersonalizadosEntidadAdmin(ImportExportModelAdmin):
    pass

@admin.register(Contrato)
class ContratoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Emoticon)
class EmoticonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Canal)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(TipoCanal)
class TipoCanalAdmin(ImportExportModelAdmin):
    pass

@admin.register(RecursosEntidad)
class RecursosEntidadAdmin(ImportExportModelAdmin):
    pass

@admin.register(ConfigRecurso)
class ConfigRecursoAdmin(ImportExportModelAdmin):
    pass

@admin.register(ListaNegra)
class ListaNegraAdmin(ImportExportModelAdmin):
    pass

@admin.register(ServiciosEntidad)
class ServiciosEntidadAdmin(ImportExportModelAdmin):
    pass

@admin.register(Pagina)
class PaginaAdmin(ImportExportModelAdmin):
    pass

@admin.register(Sucursal)
class SucursalAdmin(ImportExportModelAdmin):
    pass

@admin.register(TerminosCondiciones)
class TerminosCondicionesAdmin(ImportExportModelAdmin):
    pass

@admin.register(Intencion)
class IntencionAdmin(ImportExportModelAdmin):
    pass

@admin.register(IntencionTipo)
class IntencionTipoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Servicio)
class ServicioAdmin(ImportExportModelAdmin):
    pass