"""pjctFintech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Admin Views
from campos.admin_views import *
from entidad.admin_views import *
from mensajes.admin_views import *

urlpatterns = [
    path('admin/campos/campospersonalizadosentidad/', CamposPersonalizadosEntidadList.as_view()),
    path('admin/entidad/canal/', CanalList.as_view()),
    path('admin/entidad/entidad/', EntidadList.as_view()),
    path('admin/entidad/emoticon/', EmoticonList.as_view()),
    path('admin/entidad/intencion/', IntencionList.as_view()),
    path('admin/entidad/pagina/', PaginaList.as_view()),
    path('admin/entidad/recursosentidad/', RecursosEntidadList.as_view()),
    path('admin/entidad/sucursal/', SucursalList.as_view()),
    path('admin/entidad/terminoscondiciones/', TerminosYCondicionesList.as_view()),
    path('admin/mensajes/mensaje/', MensajeList.as_view()),
    path('admin/mensajes/mensajeerrores/', MensajesErroresList.as_view()),
    path('admin/', admin.site.urls),
]
