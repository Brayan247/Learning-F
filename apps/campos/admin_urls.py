from django.urls import path
from .views_admin import *
from .views import *
from apps.administrador.utilities import *

if(get_user_id().is_superuser == False):
    urlpatterns = [
    path('campospersonalizadosentidad/', CamposPersonalizadosEntidadList.as_view()),
    ]
else:
    urlpatterns = [
    # views
    path('', index, name='index'),
    ]