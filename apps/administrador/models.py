from django.db import models
# Utilizado para acceder a los modelos del admin
from django.contrib.auth.models import User


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
    imagen = models.ImageField()
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
    eliminado = models.IntegerField(default=0, editable=False)    

    def delete(self):
        administrador = Administrador.objects.get(idadministrador = self.idadministrador)
        administrador.eliminado = 1
        return administrador.save()

    class Meta:
        managed = True
        db_table = 'administrador'

class UserEntidad(models.Model):
    id_user_entidad = models.AutoField(db_column='id_user_entidad', primary_key=True)
    #Accederemos al modelo de User del admin
    id_user  = models.ForeignKey(User, models.DO_NOTHING, db_column = 'id_user')
    id_entidad = models.ForeignKey('entidad.Entidad', models.DO_NOTHING, db_column='id_entidad')
    eliminado = models.IntegerField(default=0, editable=False)  

    def __str__(self):
        return f"{self.id_user_entidad}{self.id_user}{self.id_entidad}" 
    
    def delete(self):
        userEntidad = UserEntidad.objects.get(id_user_entidad = self.id_user_entidad)
        userEntidad.eliminado = 1
        return userEntidad.save()

    class Meta:
        managed = True
        db_table = 'user_entidad'