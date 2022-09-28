# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    idadministrador = models.AutoField(db_column='idAdministrador', primary_key=True)  # Field name made lowercase.
    idaplicativo = models.IntegerField(db_column='idAplicativo', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(unique=True, max_length=15)
    contrasenia = models.CharField(max_length=32)
    nombres = models.CharField(max_length=125)
    apellidos = models.CharField(max_length=125)
    idpais = models.IntegerField(db_column='idPais', blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(unique=True, max_length=18)
    cedula = models.CharField(unique=True, max_length=18)
    correo = models.CharField(unique=True, max_length=125)
    hangouts = models.CharField(max_length=125)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=300)
    imagen = models.CharField(max_length=20)
    idadministradorregistro = models.IntegerField(db_column='idAdministradorRegistro', blank=True, null=True)  # Field name made lowercase.
    idadministradoredito = models.IntegerField(db_column='idAdministradorEdito', blank=True, null=True)  # Field name made lowercase.
    bloqueadomensaje = models.CharField(db_column='bloqueadoMensaje', max_length=400, blank=True, null=True)  # Field name made lowercase.
    bloqueado = models.TextField()  # This field type is a guess.
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField()
    fecha_bloqueo = models.DateTimeField(blank=True, null=True)
    fecha_reactivacion = models.DateTimeField(blank=True, null=True)
    mensajereactivacion = models.CharField(db_column='mensajeReactivacion', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tiposangre = models.CharField(db_column='tipoSangre', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cambiarclave = models.IntegerField(db_column='cambiarClave', blank=True, null=True)  # Field name made lowercase.
    clavetemporal = models.CharField(db_column='claveTemporal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fecha_cambio_clave = models.DateTimeField(blank=True, null=True)
    fecha_recupero_clave = models.DateTimeField(blank=True, null=True)
    idtipoidentificacion = models.IntegerField(db_column='idTipoIdentificacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrador'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CamposPersonalizadosEntidad(models.Model):
    entidad_identidad = models.OneToOneField('Entidad', models.DO_NOTHING, db_column='entidad_idEntidad', primary_key=True)  # Field name made lowercase.
    campos_personalizados_nueva_cuenta_idcampo = models.ForeignKey('CamposPersonalizadosNuevaCuenta', models.DO_NOTHING, db_column='campos_personalizados_nueva_cuenta_idCampo')  # Field name made lowercase.
    habilitado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'campos_personalizados_entidad'
        unique_together = (('entidad_identidad', 'campos_personalizados_nueva_cuenta_idcampo'),)


class CamposPersonalizadosNuevaCuenta(models.Model):
    idcampo = models.AutoField(db_column='idCampo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45, blank=True, null=True)
    placeholder = models.CharField(max_length=55, blank=True, null=True)
    identificador = models.CharField(max_length=55)
    requerido = models.IntegerField()
    validador = models.IntegerField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    tipo = models.ForeignKey('TiposCampos', models.DO_NOTHING, db_column='tipo')
    nopaste = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'campos_personalizados_nueva_cuenta'


class Canal(models.Model):
    idcanal = models.AutoField(db_column='idCanal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=55)
    credenciales = models.TextField(db_collation='utf8mb4_bin')
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    tipo_canal = models.ForeignKey('TipoCanal', models.DO_NOTHING, db_column='tipo_canal')
    id_entidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='id_entidad')

    class Meta:
        managed = False
        db_table = 'canal'


class CatalogosErrores(models.Model):
    idmsg_error = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'catalogos_errores'


class Ciudad(models.Model):
    idciudad = models.AutoField(db_column='idCiudad', primary_key=True)  # Field name made lowercase.
    ciudad = models.CharField(unique=True, max_length=45, db_collation='utf8mb4_0900_ai_ci', blank=True, null=True)
    acronimo = models.CharField(max_length=5)
    color = models.CharField(max_length=10)
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    limite = models.TextField(blank=True, null=True)  # This field type is a guess.
    eliminado = models.IntegerField()
    comentario = models.CharField(max_length=500)
    zonahoraria = models.CharField(db_column='zonaHoraria', max_length=6, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=100)
    id_padre = models.IntegerField()
    pais_idpais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais_idPais')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ciudad'


class ClienteBot(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    recipienteid = models.IntegerField(db_column='recipienteId', unique=True)  # Field name made lowercase.
    senderid = models.IntegerField(db_column='senderId', unique=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=45, blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    alias = models.CharField(max_length=45, blank=True, null=True)
    token = models.CharField(max_length=45, blank=True, null=True)
    medio = models.CharField(max_length=45, blank=True, null=True)
    parametro = models.IntegerField(blank=True, null=True)
    recurso = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    entidad = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    dato_extra = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    recurso_url = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente_bot'


class ClienteBotHasEntidad(models.Model):
    cliente_bot_idcliente = models.OneToOneField(ClienteBot, models.DO_NOTHING, db_column='cliente_bot_idCliente', primary_key=True)  # Field name made lowercase.
    entidad_identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='entidad_idEntidad')  # Field name made lowercase.
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente_bot_has_entidad'
        unique_together = (('cliente_bot_idcliente', 'entidad_identidad'),)


class ConfigRecurso(models.Model):
    clave = models.CharField(max_length=45)
    valor = models.TextField()
    type = models.CharField(max_length=45)
    descripcion = models.TextField()
    eliminado = models.IntegerField()
    id_recurso_entidad = models.ForeignKey('RecursosEntidad', models.DO_NOTHING, db_column='id_recurso_entidad')

    class Meta:
        managed = False
        db_table = 'config_recurso'


class Contrato(models.Model):
    idcontrato = models.AutoField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    acronimo = models.CharField(max_length=45)
    duracion = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    clausulas = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    entidad_identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='entidad_idEntidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contrato'
        unique_together = (('idcontrato', 'entidad_identidad'),)


class DetallePlan(models.Model):
    plan_idplan = models.OneToOneField('Plan', models.DO_NOTHING, db_column='plan_idPlan', primary_key=True)  # Field name made lowercase.
    modulo_idmodulo = models.IntegerField(db_column='modulo_idModulo')  # Field name made lowercase.
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_plan'
        unique_together = (('plan_idplan', 'modulo_idmodulo'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emoticon(models.Model):
    idemoticon = models.AutoField(db_column='idEmoticon', primary_key=True)  # Field name made lowercase.
    emoticon = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=2, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='idEntidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emoticon'


class Entidad(models.Model):
    identidad = models.AutoField(db_column='idEntidad', primary_key=True)  # Field name made lowercase.
    titulo_pagina = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    logo_horizontal = models.CharField(max_length=400)
    logo_vertical = models.CharField(max_length=400)
    color_primario = models.CharField(max_length=45)
    color_secundario = models.CharField(max_length=45)
    favicon = models.TextField(blank=True, null=True)
    direccion = models.CharField(max_length=400, blank=True, null=True)
    copyright = models.CharField(max_length=400, blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    lema = models.CharField(max_length=45, blank=True, null=True)
    facebook = models.CharField(max_length=45, blank=True, null=True)
    twitter = models.CharField(max_length=45, blank=True, null=True)
    activo_bot = models.IntegerField(blank=True, null=True)
    tiempo_respuesta_bot = models.IntegerField(blank=True, null=True)
    nro_intentos_fallidos = models.IntegerField(blank=True, null=True)
    tiempo_bloqueo = models.IntegerField(blank=True, null=True)
    ip_produccion = models.CharField(max_length=100, blank=True, null=True)
    ip_dev = models.CharField(max_length=100, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    ciudad_idciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_idCiudad')  # Field name made lowercase.
    respaldocliente = models.IntegerField()
    tiempo_espera_code = models.IntegerField()
    plantilla = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'entidad'


class Intencion(models.Model):
    idintencion = models.AutoField(db_column='idIntencion', primary_key=True)  # Field name made lowercase.
    intencion = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    respuesta = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    multi_mensaje = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    mensajedialogflow = models.TextField(db_column='mensajeDialogflow', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eliminado = models.IntegerField()
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    idtipointencion = models.IntegerField(db_column='idTipoIntencion')  # Field name made lowercase.
    idrecursos = models.IntegerField(db_column='idRecursos')  # Field name made lowercase.
    identidad = models.IntegerField(db_column='idEntidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'intencion'
        unique_together = (('idintencion', 'idrecursos', 'identidad'),)


class IntencionTipo(models.Model):
    idtipointencion = models.AutoField(db_column='idTipoIntencion', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'intencion_tipo'


class ListaNegra(models.Model):
    cedula = models.CharField(max_length=20)
    correo = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    intentos_actuales = models.IntegerField()
    intentos_totales = models.IntegerField()
    estado = models.IntegerField()
    id_recursos_entidad = models.ForeignKey('RecursosEntidad', models.DO_NOTHING, db_column='id_recursos_entidad')

    class Meta:
        managed = False
        db_table = 'lista_negra'


class LogsSystemFintech(models.Model):
    id_log = models.AutoField(primary_key=True)
    nombre_tabla = models.CharField(max_length=45)
    data = models.TextField(db_collation='utf8mb4_bin')
    tipo = models.CharField(max_length=45)
    idadministrador = models.CharField(db_column='idAdministrador', max_length=45)  # Field name made lowercase.
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs_system_fintech'


class Mensaje(models.Model):
    idmensaje = models.AutoField(db_column='idMensaje', primary_key=True)  # Field name made lowercase.
    mensaje = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    identidad = models.IntegerField(db_column='idEntidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mensaje'


class MensajeErrores(models.Model):
    idmensaje_error = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=250)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    id_entidad = models.IntegerField()
    id_error = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mensaje_errores'


class Modulo(models.Model):
    idmodulo = models.IntegerField(db_column='idModulo', primary_key=True)  # Field name made lowercase.
    modulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=300)
    path = models.CharField(max_length=100)
    icono = models.CharField(max_length=45)
    vista = models.CharField(max_length=45)
    orden = models.IntegerField()
    identificativo = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    idaplicativo = models.IntegerField(db_column='idAplicativo', blank=True, null=True)  # Field name made lowercase.
    idadministradorregistro = models.IntegerField(db_column='idAdministradorRegistro')  # Field name made lowercase.
    idadministradoractualizo = models.IntegerField(db_column='idAdministradorActualizo', blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    id_servicio = models.IntegerField(blank=True, null=True)
    vistapath = models.CharField(db_column='vistaPath', max_length=95)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modulo'


class ModuloPerfil(models.Model):
    idmodulo = models.IntegerField(db_column='idModulo', primary_key=True)  # Field name made lowercase.
    idperfil = models.IntegerField(db_column='idPerfil')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modulo_perfil'
        unique_together = (('idmodulo', 'idperfil'),)


class Moduloadministrador(models.Model):
    idadministrador = models.IntegerField(db_column='idAdministrador', primary_key=True)  # Field name made lowercase.
    idmodulo = models.IntegerField(db_column='idModulo')  # Field name made lowercase.
    inicio = models.IntegerField()
    leer = models.IntegerField()
    crear = models.IntegerField()
    editar = models.IntegerField()
    eliminar = models.IntegerField()
    fecha_lectura = models.DateTimeField()
    fecha_crear = models.DateTimeField(blank=True, null=True)
    fecha_editar = models.DateTimeField(blank=True, null=True)
    fecha_eliminar = models.DateTimeField(blank=True, null=True)
    idadministradorregistro = models.IntegerField(db_column='idAdministradorRegistro')  # Field name made lowercase.
    idadministradoractualizo = models.IntegerField(db_column='idAdministradorActualizo', blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moduloadministrador'
        unique_together = (('idadministrador', 'idmodulo'),)


class Moneda(models.Model):
    id_moneda = models.AutoField(primary_key=True)
    moneda = models.CharField(max_length=5)
    simbolo = models.CharField(max_length=45, blank=True, null=True)
    referencia = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=300)
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    eliminado = models.IntegerField()
    pais = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'moneda'


class OpcionesCampo(models.Model):
    idopcion = models.AutoField(db_column='idOpcion', primary_key=True)  # Field name made lowercase.
    valor = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    idcampo_opcion = models.IntegerField(db_column='idCampo_opcion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'opciones_campo'


class Pagina(models.Model):
    idpagina = models.AutoField(db_column='idPagina', primary_key=True)  # Field name made lowercase.
    identidad = models.IntegerField(db_column='idEntidad')  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    clave = models.CharField(max_length=60)
    token = models.CharField(max_length=200)
    version = models.IntegerField()
    idfacebook = models.CharField(db_column='idFacebook', max_length=45)  # Field name made lowercase.
    versionfacebook = models.CharField(db_column='versionFacebook', max_length=3)  # Field name made lowercase.
    eliminado = models.IntegerField()
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pagina'


class Pais(models.Model):
    idpais = models.AutoField(db_column='idPais', primary_key=True)  # Field name made lowercase.
    pais = models.CharField(unique=True, max_length=45)
    acronimo = models.CharField(unique=True, max_length=4)
    codigoarea = models.CharField(db_column='codigoArea', unique=True, max_length=5)  # Field name made lowercase.
    latitud = models.FloatField()
    longitud = models.FloatField()
    idadministradorregistro = models.IntegerField(db_column='idAdministradorRegistro')  # Field name made lowercase.
    idadministradoractualizo = models.IntegerField(db_column='idAdministradorActualizo', blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    eliminado = models.TextField()  # This field type is a guess.
    limite = models.TextField(blank=True, null=True)  # This field type is a guess.
    idmoneda = models.IntegerField(db_column='idMoneda', blank=True, null=True)  # Field name made lowercase.
    min_digitos_cedula = models.IntegerField(blank=True, null=True)
    max_digitos_cedula = models.IntegerField(blank=True, null=True)
    min_digitos_celular = models.IntegerField(blank=True, null=True)
    max_digitos_celular = models.IntegerField(blank=True, null=True)
    validar_cedula = models.IntegerField(blank=True, null=True)
    numericos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Perfil(models.Model):
    idperfil = models.AutoField(db_column='idPerfil', primary_key=True)  # Field name made lowercase.
    perfil = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=500)
    eliminado = models.IntegerField()
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'perfil'


class PerfilAdministrador(models.Model):
    idadministrador = models.IntegerField(db_column='idAdministrador', primary_key=True)  # Field name made lowercase.
    idperfil = models.IntegerField(db_column='idPerfil')  # Field name made lowercase.
    idadministradorregistro = models.IntegerField(db_column='idAdministradorRegistro')  # Field name made lowercase.
    idadministradorhabilito = models.IntegerField(db_column='idAdministradorHabilito', blank=True, null=True)  # Field name made lowercase.
    idadministradordeshabilito = models.IntegerField(db_column='idAdministradorDeshabilito', blank=True, null=True)  # Field name made lowercase.
    fecha_habilito = models.DateTimeField(blank=True, null=True)
    fecha_deshabilito = models.DateTimeField(blank=True, null=True)
    idadministradoractualizo = models.IntegerField(db_column='idAdministradorActualizo', blank=True, null=True)  # Field name made lowercase.
    fecha_actualizo = models.DateTimeField(blank=True, null=True)
    eliminado = models.TextField()  # This field type is a guess.
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'perfil_administrador'


class Plan(models.Model):
    idplan = models.AutoField(db_column='idPlan', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    acronimo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    costo = models.CharField(max_length=45)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plan'


class PlanContrato(models.Model):
    plan_idplan = models.IntegerField(db_column='plan_idPlan', primary_key=True)  # Field name made lowercase.
    contrato_idcontrato = models.IntegerField(db_column='contrato_idContrato')  # Field name made lowercase.
    contrato_entidad_identidad = models.IntegerField(db_column='contrato_entidad_idEntidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'plan_contrato'
        unique_together = (('plan_idplan', 'contrato_idcontrato', 'contrato_entidad_identidad'),)


class RecursosEntidad(models.Model):
    idrecursos = models.AutoField(db_column='idRecursos', primary_key=True)  # Field name made lowercase.
    path = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    param_entrada = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    param_salida = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    id_entidad = models.IntegerField()
    id_modulo = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'recursos_entidad'


class Servicio(models.Model):
    servicio = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250)
    icono = models.CharField(max_length=45)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicio'


class ServiciosEntidad(models.Model):
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    eliminado = models.IntegerField()
    id_servicio = models.IntegerField()
    id_entidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'servicios_entidad'


class Sucursal(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    referencia = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()
    tipo = models.CharField(max_length=45)
    estado = models.IntegerField()
    id_entidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class TablaTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    columna_uno = models.CharField(max_length=200)
    columna_dos = models.CharField(max_length=200)
    columna_tres = models.CharField(max_length=200)
    columna_cuatro = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tabla_test'


class TerminosCondiciones(models.Model):
    idtermino = models.AutoField(db_column='idTermino', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=550)
    descripcion = models.TextField()
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()
    entidad_identidad = models.IntegerField(db_column='entidad_idEntidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'terminos_condiciones'


class TipoCanal(models.Model):
    idtipocanal = models.AutoField(db_column='idTipoCanal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=55, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_canal'


class TiposCampos(models.Model):
    idtipo = models.AutoField(db_column='idTipo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(unique=True, max_length=45)
    descripcion = models.CharField(max_length=45)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipos_campos'
