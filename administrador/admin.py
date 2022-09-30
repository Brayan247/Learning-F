from import_export.admin import ImportExportModelAdmin
# 
from django.contrib import admin
from .models import *


@admin.register(Administrador)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthGroup)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthGroupPermissions)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthPermission)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthUser)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthUserGroups)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthUserUserPermissions)
class AdministradorAdmin(ImportExportModelAdmin):
    pass


admin.site.register(LogsSystemFintech)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)
