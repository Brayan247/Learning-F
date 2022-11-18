# User
from django.contrib.auth.models import User
# Session
from django.contrib.sessions.models import *
# Models
from apps.administrador.models import UserEntidad

def user_session_id():
    s = Session.objects.all()
    i = len(s)
    io = i-1
    se = s[io]
    session = se.get_decoded()
    auth_user_id = session['_auth_user_id']
    return auth_user_id
    
def get_user_id():
    user = User.objects.filter(id = user_session_id())
    return user[0]

def entidad_session_id(id_u):
    e = UserEntidad.objects.get(id_user=id_u)
    en = e.id_entidad
    return en

def get_entidad():
    # Id user session login
    id_user_login = user_session_id();
    #Id entidad session login
    entidad_user_login = entidad_session_id(id_user_login)
    return entidad_user_login

def get_id_entidad():
    # Id user session login
    id_user_login = user_session_id();
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
