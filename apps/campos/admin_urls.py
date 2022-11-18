from django.urls import path
from .views_admin import *
from .views import *
from apps.administrador.utilities import *

urlpatterns = [
    path('campospersonalizadosentidad/', CamposPersonalizadosEntidadList.as_view()),
    ]