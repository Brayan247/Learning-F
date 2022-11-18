from django.contrib import admin
from .models import *

def acticacion_Logica(self, request, queryset):
    for object in queryset:
        object.eliminado = 0
        object.save()

def eliminacion_Logica(self, request, queryset):
    for object in queryset:
        object.eliminado = 1
        object.save()

class EntidadAdmin(admin.ModelAdmin):
    list_display = ('identidad', 'nombre')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ContratoAdmin(admin.ModelAdmin):
    list_display = ('idcontrato', 'nombre', 'acronimo', 'duracion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class EmoticonAdmin(admin.ModelAdmin):
    list_display = ('idemoticon', 'emoticon', 'descripcion', 'codigo')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class CanalAdmin(admin.ModelAdmin):
    list_display = ('idcanal', 'nombre', 'id_entidad')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class TipoCanalAdmin(admin.ModelAdmin):
    list_display = ('idtipocanal', 'nombre', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class RecursosEntidadAdmin(admin.ModelAdmin):
    list_display = ('idrecursos','path', 'tipo', 'id_entidad')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ConfigRecursoAdmin(admin.ModelAdmin):
    list_display = ('clave', 'valor', 'type', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ListaNegraAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'correo')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ServiciosEntidadAdmin(admin.ModelAdmin):
    list_display = ('id_servicio', 'id_entidad')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class PaginaAdmin(admin.ModelAdmin):
    list_display = ('idpagina','identidad', 'nombre')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre','referencia','id_entidad')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class TerminosCondicionesAdmin(admin.ModelAdmin):
    list_display = ('idtermino','titulo', 'descripcion', 'entidad_identidad')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class IntencionAdmin(admin.ModelAdmin):
    list_display = ('idintencion', 'intencion', 'descripcion', 'identidad')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class IntencionTipoAdmin(admin.ModelAdmin):
    list_display = ('idtipointencion', 'tipo', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ServicioAdmin(admin.ModelAdmin):
    list_display = ( 'servicio', 'descripcion')
    actions = [acticacion_Logica, eliminacion_Logica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

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