from django.db import models

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
    recurso_url = models.URLField()
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'cliente_bot'

class ClienteBotHasEntidad(models.Model):
    cliente_bot_idcliente = models.OneToOneField(ClienteBot, models.DO_NOTHING, db_column='cliente_bot_idCliente', primary_key=True)  # Field name made lowercase.
    entidad_identidad = models.ForeignKey('entidad.Entidad', models.DO_NOTHING, db_column='entidad_idEntidad')  # Field name made lowercase.
    eliminado = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'cliente_bot_has_entidad'
        unique_together = (('cliente_bot_idcliente', 'entidad_identidad'),)