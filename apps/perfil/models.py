from django.db import models

class Perfil(models.Model):
    idperfil = models.AutoField(db_column='idPerfil', primary_key=True)  # Field name made lowercase.
    perfil = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=500)
    eliminado = models.IntegerField(default=0, editable=False)
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    def delete(self):
        perfil = Perfil.objects.get(idperfil = self.idperfil)
        perfil.eliminado = 1
        return perfil.save()

    class Meta:
        managed = True
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
    eliminado = models.IntegerField(default=0, editable=False)  # This field type is a guess.
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()

    def delete(self):
        pa = PerfilAdministrador.objects.get(idadministrador = self.idadministrador)
        pa.eliminado = 1
        return pa.save()

    class Meta:
        managed = True
        db_table = 'perfil_administrador'