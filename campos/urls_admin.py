from django.urls import path
from .views_admin import *
from .views import *

urlpatterns = [
    # views
    path('', index, name='index'),
    # admin views
    path('campospersonalizadosentidad/', CamposPersonalizadosEntidadList.as_view()),
]
