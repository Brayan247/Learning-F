from django.contrib import admin
from django.urls import include, path 
# Admin Views

urlpatterns = [
    path('admin/campos/', include('campos.urls_admin')),
    path('admin/entidad/', include('entidad.urls_admin')),
    path('admin/mensajes/', include('mensajes.urls_admin')),
    path('admin/', admin.site.urls),
]
