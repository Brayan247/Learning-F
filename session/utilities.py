# Session
from django.contrib.sessions.models import Session
# Models
from administrador.models import *
from entidad.models import Entidad

def user_session_id():
    s = Session.objects.all()
    if (s == any) :
        return any
    else:
        i = len(s)
        io = i-1
        se = s[io]
        session = se.get_decoded()
        auth_user_id = session['_auth_user_id']
        return auth_user_id
    
print(user_session_id())

def entidad_session_id(id_u):
    e = UserEntidad.objects.get(id_user=id_u)
    en = e.id_entidad
    entidad = Entidad.objects.get(identidad=en)
    entidad_id = entidad.identidad
    return entidad_id

def id_entidad():
    # Id user session login
    id_user_login = user_session_id();
    #Id entidad session login
    id_entidad_user_login = entidad_session_id(id_user_login)
    return id_entidad_user_login

print(id_entidad)