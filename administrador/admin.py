# Sessions
from cgi import print_directory
from django.contrib.sessions.models import Session
from entidad.models import Entidad
#
from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
from .models import *

def user_session_id():
    s = Session.objects.get()
    session = s.get_decoded()
    auth_user_id = session['_auth_user_id']
    return auth_user_id

def entidad_session_id(id_u):
    e = UserEntidad.objects.get(id_user=id_u)
    en = e.id_entidad
    ent = en.identidad
    entidad = Entidad.objects.get(identidad=ent)
    entidad_id = entidad.identidad
    return entidad_id

# Id user session login
id_user_login = user_session_id();

#Id entidad session login
id_entidad_user_login = entidad_session_id(id_user_login)

@admin.register(Administrador)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(UserEntidad)
class UserEntidadAdmin(ImportExportModelAdmin):
    pass