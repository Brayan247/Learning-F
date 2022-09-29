from django.db import models

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