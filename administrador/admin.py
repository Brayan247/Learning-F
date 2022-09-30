from import_export.admin import ImportExportModelAdmin
# 
from django.contrib import admin
from .models import *


@admin.register(Administrador)
class AdministradorAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthGroup)
class AuthGroupAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthGroupPermissions)
class AuthGroupPermissionsAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthPermission)
class AuthPermissionAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthUser)
class AuthUserAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthUserGroups)
class AuthUserGroupsAdmin(ImportExportModelAdmin):
    pass

@admin.register(AuthUserUserPermissions)
class AuthUserUserPermissionsAdmin(ImportExportModelAdmin):
    pass

@admin.register(LogsSystemFintech)
class LogsSystemFintechAdmin(ImportExportModelAdmin):
    pass

@admin.register(DjangoAdminLog)
class DjangoAdminLogAdmin(ImportExportModelAdmin):
    pass

@admin.register(DjangoContentType)
class DjangoContentTypeAdmin(ImportExportModelAdmin):
    pass

@admin.register(DjangoMigrations)
class DjangoMigrationsAdmin(ImportExportModelAdmin):
    pass

@admin.register(DjangoSession)
class DjangoSessionAdmin(ImportExportModelAdmin):
    pass

