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
    eliminado = models.IntegerField(default=0, editable=False)
    tipo = models.ForeignKey('TiposCampos', models.DO_NOTHING, db_column='tipo')
    nopaste = models.IntegerField()

    def delete(self):
        cpnc = CamposPersonalizadosNuevaCuenta.objects.get(idcampo = self.idcampo)
        cpnc.eliminado = 1
        return cpnc.save()

    def __str__(self):
        return f"{self.nombre}"     

    class Meta:
        managed = True
        db_table = 'campos_personalizados_nueva_cuenta'

class CamposPersonalizadosEntidad(models.Model):
    entidad_identidad = models.OneToOneField('entidad.Entidad', models.DO_NOTHING, db_column='entidad_idEntidad', primary_key=True)  # Field name made lowercase. 
    campos_personalizados_nueva_cuenta_idcampo = models.ForeignKey('CamposPersonalizadosNuevaCuenta', models.DO_NOTHING, db_column='campos_personalizados_nueva_cuenta_idCampo')  # Field name made lowercase.
    habilitado = models.IntegerField()
    eliminado = models.IntegerField(default=0, editable=False)

    def delete(self):
        cpe = CamposPersonalizadosEntidad.objects.get(entidad_identidad = self.entidad_identidad)
        cpe.eliminado = 1
        return cpe.save()

    class Meta:
        managed = True
        db_table = 'campos_personalizados_entidad'
        unique_together = (('entidad_identidad', 'campos_personalizados_nueva_cuenta_idcampo'),)

class TiposCampos(models.Model):
    idtipo = models.AutoField(db_column='idTipo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(unique=True, max_length=45)
    descripcion = models.CharField(max_length=45)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)

    def delete(self):
        tc = TiposCampos.objects.get(idtipo = self.idtipo)
        tc.eliminado = 1
        return tc.save()

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        managed = True
        db_table = 'tipos_campos'

class OpcionesCampo(models.Model):
    idopcion = models.AutoField(db_column='idOpcion', primary_key=True)  # Field name made lowercase.
    valor = models.CharField(max_length=45)
    nombre = models.CharField(max_length=45)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    idcampo_opcion = models.IntegerField(db_column='idCampo_opcion')  # Field name made lowercase.

    def delete(self):
        oc = OpcionesCampo.objects.get(idopcion = self.idopcion)
        oc.eliminado = 1
        return oc.save()

    class Meta:
        managed = True
        db_table = 'opciones_campo'

