from django.views.generic import ListView
#
from .models import *
#
from apps.administrador.utilities import *

class MensajeList(ListView):
    context_object_name = 'mensaje_list'
    template_name = 'mensajes/mensaje_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  Mensaje.objects.all()
    else:
        queryset =  Mensaje.objects.all().filter(identidad = get_id_entidad()).filter(eliminado = 0)

class MensajesErroresList(ListView):
    context_object_name = 'me_list'
    template_name = 'mensajes/mensajeserrores_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  MensajeErrores.objects.all()
    else:
        queryset =  MensajeErrores.objects.all().filter(id_entidad = get_id_entidad()).filter(eliminado = 0)
        