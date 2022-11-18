from django.views.generic import ListView
#
from .models import *
#
from apps.administrador.utilities import *

class CanalList(ListView):
    context_object_name = 'canal_list'
    template_name = 'entidad/canal_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  Canal.objects.all()
            return queryset
        else:
            queryset =  Canal.objects.all().filter(id_entidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset
        
class EntidadList(ListView):
    context_object_name = 'entidad_list'
    template_name = 'entidad/entidad_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  Entidad.objects.all()
            return queryset
        else:
            queryset =  Entidad.objects.all().filter(identidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset
        
class EmoticonList(ListView):
    context_object_name = 'emoticon_list'
    template_name = 'entidad/emoticon_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  Emoticon.objects.all()
            return queryset
        else:
            queryset =  Emoticon.objects.all().filter(identidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset

class PaginaList(ListView):
    context_object_name = 'pagina_list'
    template_name = 'entidad/pagina_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  Pagina.objects.all()
            return queryset
        else:
            queryset =  Pagina.objects.all().filter(identidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset
        
class RecursosEntidadList(ListView):
    context_object_name = 're_list'
    template_name = 'entidad/recursosentidad_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  RecursosEntidad.objects.all()
            return queryset
        else:
            queryset =  RecursosEntidad.objects.all().filter(id_entidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset

class SucursalList(ListView):
    context_object_name = 'sucursal_list'
    template_name = 'entidad/sucursal_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  Sucursal.objects.all()
            return queryset
        else:
            queryset =  Sucursal.objects.all().filter(id_entidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset

class TerminosYCondicionesList(ListView):
    context_object_name = 'tyc_list'
    template_name = 'entidad/terminosycondiciones_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  TerminosCondiciones.objects.all()
            return queryset
        else:
            queryset =  TerminosCondiciones.objects.all().filter(entidad_identidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset

class IntencionList(ListView):
    context_object_name = 'intencion_list'
    template_name = 'entidad/intencion_list.html'
    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  Intencion.objects.all()
            return queryset
        else:
            queryset =  Intencion.objects.all().filter(identidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset

