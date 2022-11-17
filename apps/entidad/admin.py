from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

@admin.register(Entidad)
class EntidadAdmin(ImportExportModelAdmin):
    list_display = ('identidad', 'nombre')
    pass

@admin.register(Contrato)
class ContratoAdmin(ImportExportModelAdmin):
    list_display = ('idcontrato', 'nombre', 'acronimo', 'duracion')
    pass

@admin.register(Emoticon)
class EmoticonAdmin(ImportExportModelAdmin):
    list_display = ('idemoticon', 'emoticon', 'descripcion', 'codigo')
    pass

@admin.register(Canal)
class AdministradorAdmin(ImportExportModelAdmin):
    list_display = ('idcanal', 'nombre', 'id_entidad')
    pass

@admin.register(TipoCanal)
class TipoCanalAdmin(ImportExportModelAdmin):
    list_display = ('idtipocanal', 'nombre', 'descripcion')
    pass

@admin.register(RecursosEntidad)
class RecursosEntidadAdmin(ImportExportModelAdmin):
    list_display = ('idrecursos','path', 'tipo', 'id_entidad')
    pass

@admin.register(ConfigRecurso)
class ConfigRecursoAdmin(ImportExportModelAdmin):
    list_display = ('clave', 'valor', 'type', 'descripcion')
    pass

@admin.register(ListaNegra)
class ListaNegraAdmin(ImportExportModelAdmin):
    list_display = ('cedula', 'correo')
    pass

@admin.register(ServiciosEntidad)
class ServiciosEntidadAdmin(ImportExportModelAdmin):
    list_display = ('id_servicio', 'id_entidad')
    pass

@admin.register(Pagina)
class PaginaAdmin(ImportExportModelAdmin):
    list_display = ('idpagina','identidad', 'nombre')
    pass

@admin.register(Sucursal)
class SucursalAdmin(ImportExportModelAdmin):
    list_display = ('nombre','referencia','id_entidad')
    pass

@admin.register(TerminosCondiciones)
class TerminosCondicionesAdmin(ImportExportModelAdmin):
    list_display = ('idtermino','titulo', 'descripcion', 'entidad_identidad')
    pass

@admin.register(Intencion)
class IntencionAdmin(ImportExportModelAdmin):
    list_display = ('idintencion', 'intencion', 'descripcion', 'identidad')
    pass

@admin.register(IntencionTipo)
class IntencionTipoAdmin(ImportExportModelAdmin):
    list_display = ('idtipointencion', 'tipo', 'descripcion')
    pass

@admin.register(Servicio)
class ServicioAdmin(ImportExportModelAdmin):
    list_display = ( 'servicio', 'descripcion')
    pass