from django.views.generic import ListView
#
from .models import *
#
from administrador.utilities import *

class CamposPersonalizadosEntidadList(ListView):
    context_object_name = 'cpe_list'
    template_name = 'campos_personalizados_entidad_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  CamposPersonalizadosEntidad.objects.all()
    else:
        queryset =  CamposPersonalizadosEntidad.objects.all().filter(entidad_identidad = get_id_entidad()).filter(eliminado = 0)
    