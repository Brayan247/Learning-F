from django.contrib import admin
from django.urls import include, path 
# Admin Views

urlpatterns = [
    path('admin/campos/', include('apps.campos.admin_urls')),
    path('admin/entidad/', include('apps.entidad.admin_urls')),
    path('admin/mensajes/', include('apps.mensajes.admin_urls')),
    path('admin/', admin.site.urls),
]
