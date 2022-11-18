# User
from django.contrib.auth.models import User
# Session
from django.contrib.sessions.models import *
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

def acticacion_Logica(self, request, queryset):
    for object in queryset:
        object.eliminado = 0
        object.save()

def eliminacion_Logica(self, request, queryset):
    for object in queryset:
        object.eliminado = 1
        object.save()
