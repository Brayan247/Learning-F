from django.views.generic import ListView
#
from .models import *
#
from administrador.utilities import *

class MensajeList(ListView):
    context_object_name = 'mensaje_list'
    template_name = 'mensaje_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  Mensaje.objects.all()
    else:
        queryset =  Mensaje.objects.all().filter(identidad = get_id_entidad())

class MensajesErroresList(ListView):
    context_object_name = 'me_list'
    template_name = 'mensajeserrores_list.html'
    if(get_user_id().is_superuser == True):
        queryset =  MensajeErrores.objects.all()
    else:
        queryset =  MensajeErrores.objects.all().filter(id_entidad = get_id_entidad())
        