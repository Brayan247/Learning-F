from django.views.generic import ListView
#
from .models import *
#
from apps.administrador.utilities import *

class CamposPersonalizadosEntidadList(ListView):
    context_object_name = 'cpe_list'
    template_name = 'admin/campos/campos_personalizados_entidad_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  CamposPersonalizadosEntidad.objects.all()
            return queryset
        else:
            queryset =  CamposPersonalizadosEntidad.objects.filter(entidad_identidad = get_id_entidad(user), eliminado = 0)
            return queryset
        