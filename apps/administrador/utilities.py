# Models
from apps.administrador.models import UserEntidad

def entidad_session_id(id_u):
    e = UserEntidad.objects.get(id_user=id_u)
    en = e.id_entidad
    return en

def get_id_entidad(id_user_login):
    #Id entidad session login
    entidad_user_login = entidad_session_id(id_user_login)
    return entidad_user_login.identidad

def activacionLogica(self, request, queryset):
    for object in queryset:
        object.eliminado = 0
        object.save()

def eliminacionLogica(self, request, queryset):
    for object in queryset:
        object.eliminado = 1
        object.save()

class ParentAdmin:
    actions = [activacionLogica, eliminacionLogica]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions