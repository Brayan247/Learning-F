# Session
from django.contrib.sessions.models import Session
# Models
from administrador.models import UserEntidad

def user_session_id():
    s = Session.objects.all()
    i = len(s)
    io = i-1
    se = s[io]
    session = se.get_decoded()
    auth_user_id = session['_auth_user_id']
    return auth_user_id
    

def entidad_session_id(id_u):
    e = UserEntidad.objects.get(id_user=id_u)
    en = e.id_entidad
    return en

def id_entidad():
    # Id user session login
    id_user_login = user_session_id();
    #Id entidad session login
    entidad_user_login = entidad_session_id(id_user_login)
    return entidad_user_login
