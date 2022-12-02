from django.db import models

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
    eliminado = models.IntegerField(default=0, editable=False)  # This field type is a guess.
    limite = models.TextField(blank=True, null=True)  # This field type is a guess.
    idmoneda = models.IntegerField(db_column='idMoneda', blank=True, null=True)  # Field name made lowercase.
    min_digitos_cedula = models.IntegerField(blank=True, null=True)
    max_digitos_cedula = models.IntegerField(blank=True, null=True)
    min_digitos_celular = models.IntegerField(blank=True, null=True)
    max_digitos_celular = models.IntegerField(blank=True, null=True)
    validar_cedula = models.IntegerField(blank=True, null=True)
    numericos = models.IntegerField(blank=True, null=True)

    def delete(self):
        pais = Pais.objects.get(idpais = self.idpais)
        pais.eliminado = 1
        return pais.save()

    class Meta:
        managed = True
        db_table = 'pais'
    
    def __str__(self):
        return f"{self.pais}"

class Moneda(models.Model):
    id_moneda = models.AutoField(primary_key=True)
    moneda = models.CharField(max_length=5)
    simbolo = models.CharField(max_length=45, blank=True, null=True)
    referencia = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=300)
    fecha_registro = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField()
    eliminado = models.IntegerField(default=0, editable=False)
    pais = models.IntegerField()

    def delete(self):
        moneda = Moneda.objects.get(id_moneda = self.id_moneda)
        moneda.eliminado = 1
        return moneda.save()

    class Meta:
        managed = True
        db_table = 'moneda'

    def __str__(self):
        return f"{self.moneda}"

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
    eliminado = models.IntegerField(default=0, editable=False)
    comentario = models.CharField(max_length=500)
    zonahoraria = models.CharField(db_column='zonaHoraria', max_length=6, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=100)
    id_padre = models.IntegerField()
    pais_idpais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais_idPais')  # Field name made lowercase.

    def delete(self):
        ciudad = Ciudad.objects.get(idciudad = self.idciudad)
        ciudad.eliminado = 1
        return ciudad.save()

    def __str__(self):
        return f"{self.ciudad}"

    class Meta:
        managed = True
        db_table = 'ciudad'