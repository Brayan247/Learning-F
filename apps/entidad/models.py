from contextlib import nullcontext
from email.policy import default
from django.db import models

class Entidad(models.Model):
    identidad = models.AutoField(db_column='idEntidad', primary_key=True)  # Field name made lowercase.
    titulo_pagina = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    logo_horizontal = models.ImageField()
    logo_vertical = models.ImageField()
    color_primario = models.CharField(max_length=45)
    color_secundario = models.CharField(max_length=45)
    favicon = models.URLField(blank=True, null=True)
    direccion = models.CharField(max_length=400, blank=True, null=True)
    copyright = models.CharField(max_length=400, blank=True, null=True)
    contacto = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45, blank=True, null=True)
    lema = models.CharField(max_length=45, blank=True, null=True)
    facebook = models.URLField(max_length=45, blank=True, null=True)
    twitter = models.URLField(max_length=45, blank=True, null=True)
    activo_bot = models.IntegerField(blank=True, null=True)
    tiempo_respuesta_bot = models.IntegerField(blank=True, null=True)
    nro_intentos_fallidos = models.IntegerField(blank=True, null=True)
    tiempo_bloqueo = models.IntegerField(blank=True, null=True)
    ip_produccion = models.CharField(max_length=100, blank=True, null=True)
    ip_dev = models.CharField(max_length=100, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    ciudad_idciudad = models.ForeignKey('pais.Ciudad', models.DO_NOTHING, db_column='ciudad_idCiudad')  # Field name made lowercase.
    respaldocliente = models.IntegerField()
    tiempo_espera_code = models.IntegerField()
    plantilla = models.IntegerField()

    def delete(self):
        entidad = Entidad.objects.get(identidad = self.identidad)
        entidad.eliminado = 1
        return entidad.save()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        managed = True
        db_table = 'entidad'

class Canal(models.Model):
    idcanal = models.AutoField(db_column='idCanal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=55)
    credenciales = models.TextField(db_collation='utf8mb4_bin')
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    tipo_canal = models.ForeignKey('TipoCanal', models.DO_NOTHING, db_column='tipo_canal')
    id_entidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='id_entidad')

    def delete(self):
        canal = Canal.objects.get(idcanal = self.idcanal)
        canal.eliminado = 1
        return canal.save()

    class Meta:
        managed = True
        db_table = 'canal'

class TipoCanal(models.Model):
    idtipocanal = models.AutoField(db_column='idTipoCanal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=55, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)

    def delete(self):
        tipocanal = TipoCanal.objects.get(idtipocanal = self.idtipocanal)
        tipocanal.eliminado = 1
        return tipocanal.save()

    class Meta:
        managed = True
        db_table = 'tipo_canal'

class Contrato(models.Model):
    idcontrato = models.AutoField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    acronimo = models.CharField(max_length=45)
    duracion = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    clausulas = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    entidad_identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='entidad_idEntidad')  # Field name made lowercase.

    def delete(self):
        contrato = Contrato.objects.get(idcontrato = self.idcontrato)
        contrato.eliminado = 1
        return contrato.save()

    class Meta:
        managed = True
        db_table = 'contrato'
        unique_together = (('idcontrato', 'entidad_identidad'),)

class Emoticon(models.Model):
    idemoticon = models.AutoField(db_column='idEmoticon', primary_key=True)  # Field name made lowercase.
    emoticon = models.ImageField()
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=2, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    identidad = models.ForeignKey('Entidad', models.DO_NOTHING, db_column='idEntidad')  # Field name made lowercase.

    def delete(self):
        emoticon = Emoticon.objects.get(idemoticon = self.idemoticon)
        emoticon.eliminado = 1
        return emoticon.save()

    class Meta:
        managed = True
        db_table = 'emoticon'

class RecursosEntidad(models.Model):
    idrecursos = models.AutoField(db_column='idRecursos', primary_key=True)  # Field name made lowercase.
    path = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    param_entrada = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    param_salida = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    id_entidad = models.IntegerField()
    id_modulo = models.IntegerField(unique=True)

    def delete(self):
        re = RecursosEntidad.objects.get(idrecursos = self.idrecursos)
        re.eliminado = 1
        return re.save()

    class Meta:
        managed = True
        db_table = 'recursos_entidad'

class ConfigRecurso(models.Model):
    clave = models.CharField(max_length=45)
    valor = models.TextField()
    type = models.CharField(max_length=45)
    descripcion = models.TextField()
    eliminado = models.IntegerField(default=0, editable=False)
    id_recurso_entidad = models.ForeignKey('RecursosEntidad', models.DO_NOTHING, db_column='id_recurso_entidad')

    def delete(self):
        cr = ConfigRecurso.objects.get(clave = self.clave)
        cr.eliminado = 1
        return cr.save()

    class Meta:
        managed = True
        db_table = 'config_recurso'

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
    eliminado = models.IntegerField(default = 0, editable=False)

    def delete(self):
        ln = ListaNegra.objects.get(cedula = self.cedula)
        ln.eliminado = 1
        return ln.save()

    class Meta:
        managed = True
        db_table = 'lista_negra'

class ServiciosEntidad(models.Model):
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    id_servicio = models.IntegerField()
    id_entidad = models.IntegerField()

    def delete(self):
        se = ServiciosEntidad.objects.get(id = self.pk)
        se.eliminado = 1
        return se.save()

    class Meta:
        managed = True
        db_table = 'servicios_entidad'

class Pagina(models.Model):
    idpagina = models.AutoField(db_column='idPagina', primary_key=True)  # Field name made lowercase.
    identidad = models.IntegerField(db_column='idEntidad')  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    clave = models.CharField(max_length=60)
    token = models.CharField(max_length=200)
    version = models.IntegerField()
    idfacebook = models.CharField(db_column='idFacebook', max_length=45)  # Field name made lowercase.
    versionfacebook = models.CharField(db_column='versionFacebook', max_length=3)  # Field name made lowercase.
    eliminado = models.IntegerField(default=0, editable=False)
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    def delete(self):
        pagina = Pagina.objects.get(idpagina = self.idpagina)
        pagina.eliminado = 1
        return pagina.save()

    class Meta:
        managed = True
        db_table = 'pagina'

class Sucursal(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    referencia = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()
    tipo = models.CharField(max_length=45)
    estado = models.IntegerField()
    id_entidad = models.IntegerField()
    eliminado = models.IntegerField(default=0, editable=False)

    def delete(self):
        sucursal = Sucursal.objects.get(id = self.pk)
        sucursal.eliminado = 1
        return sucursal.save()

    class Meta:
        managed = True
        db_table = 'sucursal'

class TerminosCondiciones(models.Model):
    idtermino = models.AutoField(db_column='idTermino', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=550)
    descripcion = models.TextField()
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    entidad_identidad = models.IntegerField(db_column='entidad_idEntidad')  # Field name made lowercase.

    def delete(self):
        tc = TerminosCondiciones.objects.get(idtermino = self.idtermino)
        tc.eliminado = 1
        return tc.save()

    class Meta:
        managed = True
        db_table = 'terminos_condiciones'

class Intencion(models.Model):
    idintencion = models.AutoField(db_column='idIntencion', primary_key=True)  # Field name made lowercase.
    intencion = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    respuesta = models.TextField(db_collation='utf8mb4_bin', blank=True, null=True)
    multi_mensaje = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    mensajedialogflow = models.TextField(db_column='mensajeDialogflow', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eliminado = models.IntegerField(default=0, editable=False)
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    idtipointencion = models.IntegerField(db_column='idTipoIntencion')  # Field name made lowercase.
    idrecursos = models.IntegerField(db_column='idRecursos')  # Field name made lowercase.
    identidad = models.IntegerField(db_column='idEntidad')  # Field name made lowercase.

    def delete(self):
        intencion = Intencion.objects.get(idintencion = self.idintencion)
        intencion.eliminado = 1
        return intencion.save()

    class Meta:
        managed = True
        db_table = 'intencion'
        unique_together = (('idintencion', 'idrecursos', 'identidad'),)


class IntencionTipo(models.Model):
    idtipointencion = models.AutoField(db_column='idTipoIntencion', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)

    def delete(self):
        it = IntencionTipo.objects.get(idtipointencion = self.idtipointencion)
        it.eliminado = 1
        return it.save()

    class Meta:
        managed = True
        db_table = 'intencion_tipo'

class Servicio(models.Model):
    servicio = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=250)
    icono = models.CharField(max_length=45)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)

    def delete(self):
        servicio = Servicio.objects.get(id = self.pk)
        servicio.eliminado = 1
        return servicio.save()

    class Meta:
        managed = True
        db_table = 'servicio'