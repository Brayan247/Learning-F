from django.db import models

class Modulo(models.Model):
    idmodulo = models.IntegerField(db_column='idModulo', primary_key=True)  # Field name made lowercase.
    modulo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=300)
    path = models.CharField(max_length=100)
    icono = models.ImageField()
    vista = models.CharField(max_length=45)
    orden = models.IntegerField()
    identificativo = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    idaplicativo = models.IntegerField(db_column='idAplicativo', blank=True, null=True)  # Field name made lowercase.
    idadministradorregistro = models.IntegerField(db_column='idAdministradorRegistro')  # Field name made lowercase.
    idadministradoractualizo = models.IntegerField(db_column='idAdministradorActualizo', blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)
    id_servicio = models.IntegerField(blank=True, null=True)
    vistapath = models.CharField(db_column='vistaPath', max_length=95)  # Field name made lowercase.

    def delete(self):
        modulo = Modulo.objects.get(idmodulo = self.idmodulo)
        modulo.eliminado = 1
        return modulo.save()

    class Meta:
        managed = True
        db_table = 'modulo'


class ModuloPerfil(models.Model):
    idmodulo = models.IntegerField(db_column='idModulo', primary_key=True)  # Field name made lowercase.
    idperfil = models.IntegerField(db_column='idPerfil')  # Field name made lowercase.
    eliminado = models.IntegerField(default=0, editable=False)

    def delete(self):
        mp = ModuloPerfil.objects.get(idmodulo = self.idmodulo)
        mp.eliminado = 1
        return mp.save()

    class Meta:
        managed = True
        db_table = 'modulo_perfil'
        unique_together = (('idmodulo', 'idperfil'),)


class Moduloadministrador(models.Model):
    idadministrador = models.IntegerField(db_column='idAdministrador', primary_key=True)  # Field name made lowercase.
    idmodulo = models.IntegerField(db_column='idModulo')  # Field name made lowercase.
    inicio = models.IntegerField()
    leer = models.IntegerField()
    crear = models.IntegerField()
    editar = models.IntegerField()
    eliminado = models.IntegerField(default=0, editable=False)
    fecha_lectura = models.DateTimeField()
    fecha_crear = models.DateTimeField(blank=True, null=True)
    fecha_editar = models.DateTimeField(blank=True, null=True)
    fecha_eliminar = models.DateTimeField(blank=True, null=True)
    idadministradorregistro = models.IntegerField(db_column='idAdministradorRegistro')  # Field name made lowercase.
    idadministradoractualizo = models.IntegerField(db_column='idAdministradorActualizo', blank=True, null=True)  # Field name made lowercase.
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)

    def delete(self):
        ma = Moduloadministrador.objects.get(idadministrador = self.idadministrador)
        ma.eliminado = 1
        return ma.save()

    class Meta:
        managed = True
        db_table = 'moduloadministrador'
        unique_together = (('idadministrador', 'idmodulo'),)