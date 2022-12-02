from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from apps.administrador.utilities import ParentAdmin

class EntidadAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('identidad', 'nombre', 'eliminado')

class ContratoAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idcontrato', 'nombre', 'acronimo', 'duracion', 'eliminado')

class EmoticonAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idemoticon', 'emoticon', 'eliminado')

class CanalAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idcanal', 'nombre', 'id_entidad', 'eliminado')

class TipoCanalAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idtipocanal', 'nombre', 'eliminado')

class RecursosEntidadAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idrecursos','path', 'tipo', 'id_entidad', 'eliminado')

class ConfigRecursoAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('clave', 'valor', 'eliminado')

class ListaNegraAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cedula', 'correo', 'eliminado')

class ServiciosEntidadAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id_servicio', 'id_entidad', 'eliminado')

class PaginaAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idpagina','identidad', 'nombre', 'eliminado')

class SucursalAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre','referencia','id_entidad', 'eliminado')

class TerminosCondicionesAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idtermino','titulo', 'entidad_identidad', 'eliminado')

class IntencionAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idintencion', 'intencion', 'identidad', 'eliminado')

class IntencionTipoAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('idtipointencion', 'tipo', 'eliminado')

class ServicioAdmin(ParentAdmin, ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ( 'servicio', 'descripcion', 'eliminado')

admin.site.register(Canal, CanalAdmin)
admin.site.register(Entidad, EntidadAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Emoticon, EmoticonAdmin)
admin.site.register(TipoCanal, TipoCanalAdmin)
admin.site.register(RecursosEntidad, RecursosEntidadAdmin)
admin.site.register(ConfigRecurso, ConfigRecursoAdmin)
admin.site.register(ListaNegra, ListaNegraAdmin)
admin.site.register(ServiciosEntidad, ServiciosEntidadAdmin)
admin.site.register(Pagina, PaginaAdmin)
admin.site.register(Sucursal, SucursalAdmin)
admin.site.register(TerminosCondiciones, TerminosCondicionesAdmin)
admin.site.register(Intencion, IntencionAdmin)
admin.site.register(IntencionTipo, IntencionTipoAdmin)
admin.site.register(Servicio, ServicioAdmin)