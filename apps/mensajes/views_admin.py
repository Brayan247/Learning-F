from django.views.generic import ListView
#
from .models import *
#
from apps.administrador.utilities import *

class MensajeList(ListView):
    context_object_name = 'mensaje_list'
    template_name = 'mensajes/mensaje_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  Mensaje.objects.all()
            return queryset
        else:
            queryset =  Mensaje.objects.all().filter(identidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset

class MensajesErroresList(ListView):
    context_object_name = 'me_list'
    template_name = 'mensajes/mensajeserrores_list.html'

    def get_queryset(self):
        user = self.request.user
        if(user.is_superuser):
            queryset =  MensajeErrores.objects.all()
            return queryset
        else:
            queryset =  MensajeErrores.objects.all().filter(id_entidad = get_id_entidad(user)).filter(eliminado = 0)
            return queryset
        