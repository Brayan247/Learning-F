from django.db import models

class Mensaje(models.Model):
    idmensaje = models.AutoField(db_column='idMensaje', primary_key=True)  # Field name made lowercase.
    mensaje = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0)
    identidad = models.IntegerField(db_column='idEntidad')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'mensaje'

class MensajeErrores(models.Model):
    idmensaje_error = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=250)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0)
    id_entidad = models.IntegerField()
    id_error = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'mensaje_errores'

class CatalogosErrores(models.Model):
    idmsg_error = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'catalogos_errores'