from django.db import models

class Mensaje(models.Model):
    idmensaje = models.AutoField(db_column='idMensaje', primary_key=True)  # Field name made lowercase.
    mensaje = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45, blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    identidad = models.IntegerField(db_column='idEntidad')  # Field name made lowercase.

    def delete(self):
        mensaje = Mensaje.objects.get(idmensaje = self.idmensaje)
        mensaje.eliminado = 1
        return mensaje.save()

    class Meta:
        managed = True
        db_table = 'mensaje'

class MensajeErrores(models.Model):
    idmensaje_error = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=250)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    id_entidad = models.IntegerField()
    id_error = models.IntegerField()

    def delete(self):
        me = MensajeErrores.objects.get(idmensaje_error = self.idmensaje_error)
        me.eliminado = 1
        return me.save()

    class Meta:
        managed = True
        db_table = 'mensaje_errores'

class CatalogosErrores(models.Model):
    idmsg_error = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)

    def delete(self):
        ce = CatalogosErrores.objects.get(idmsg_error = self.idmsg_error)
        ce.eliminado = 1
        return ce.save()

    class Meta:
        managed = True
        db_table = 'catalogos_errores'