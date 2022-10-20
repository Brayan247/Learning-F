from django.views.generic import ListView
#
from .models import *
#
from administrador.utilities import *

class CanalList(ListView):
    context_object_name = 'canal_list'
    template_name = 'canal_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  Canal.objects.all()
    else:
        queryset =  Canal.objects.all().filter(id_entidad = get_id_entidad())
        
class EntidadList(ListView):
    context_object_name = 'entidad_list'
    template_name = 'entidad_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  Entidad.objects.all()
    else:
        queryset =  Entidad.objects.all().filter(identidad = get_id_entidad())
        
class EmoticonList(ListView):
    context_object_name = 'emoticon_list'
    template_name = 'emoticon_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  Emoticon.objects.all()
    else:
        queryset =  Emoticon.objects.all().filter(identidad = get_id_entidad())

class PaginaList(ListView):
    context_object_name = 'pagina_list'
    template_name = 'pagina_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  Pagina.objects.all()
    else:
        queryset =  Pagina.objects.all().filter(identidad = get_id_entidad())
        
class RecursosEntidadList(ListView):
    context_object_name = 're_list'
    template_name = 'recursosentidad_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  RecursosEntidad.objects.all()
    else:
        queryset =  RecursosEntidad.objects.all().filter(id_entidad = get_id_entidad())

class SucursalList(ListView):
    context_object_name = 'sucursal_list'
    template_name = 'sucursal_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  Sucursal.objects.all()
    else:
        queryset =  Sucursal.objects.all().filter(id_entidad = get_id_entidad())

class TerminosYCondicionesList(ListView):
    context_object_name = 'tyc_list'
    template_name = 'terminosycondiciones_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  TerminosCondiciones.objects.all()
    else:
        queryset =  TerminosCondiciones.objects.all().filter(entidad_identidad = get_id_entidad())

class IntencionList(ListView):
    context_object_name = 'intencion_list'
    template_name = 'intencion_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  Intencion.objects.all()
    else:
        queryset =  Intencion.objects.all().filter(identidad = get_id_entidad())

