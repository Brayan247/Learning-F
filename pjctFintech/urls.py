from django.contrib import admin
from django.urls import include, path 
from apps import *
# Admin Views

urlpatterns = [
    path('admin/campos/', include('apps.campos.urls_admin')),
    path('admin/entidad/', include('apps.entidad.urls_admin')),
    path('admin/mensajes/', include('apps.mensajes.urls_admin')),
    path('admin/', admin.site.urls),
]
