from django.urls import path
from .views_admin import *
from .views import *

urlpatterns = [
    # admin views
    path('entidad/', EntidadList.as_view()),
    path('emoticon/', EmoticonList.as_view()),
    path('intencion/', IntencionList.as_view()),
    path('pagina/', PaginaList.as_view()),
    path('recursosentidad/', RecursosEntidadList.as_view()),
    path('sucursal/', SucursalList.as_view()),
    path('terminoscondiciones/', TerminosYCondicionesList.as_view()),
    path('canal/', CanalList.as_view()),
]
