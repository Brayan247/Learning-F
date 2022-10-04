from django.db import models

class Plan(models.Model):
    idplan = models.AutoField(db_column='idPlan', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    acronimo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=45)
    costo = models.CharField(max_length=45)
    fecha_actualizacion = models.DateTimeField()
    fecha_registro = models.DateTimeField()
    eliminado = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'plan'

class DetallePlan(models.Model):
    plan_idplan = models.OneToOneField('Plan', models.DO_NOTHING, db_column='plan_idPlan', primary_key=True)  # Field name made lowercase.
    modulo_idmodulo = models.IntegerField(db_column='modulo_idModulo')  # Field name made lowercase.
    eliminado = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'detalle_plan'
        unique_together = (('plan_idplan', 'modulo_idmodulo'),)

class PlanContrato(models.Model):
    plan_idplan = models.IntegerField(db_column='plan_idPlan', primary_key=True)  # Field name made lowercase.
    contrato_idcontrato = models.IntegerField(db_column='contrato_idContrato')  # Field name made lowercase.
    contrato_entidad_identidad = models.IntegerField(db_column='contrato_entidad_idEntidad')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'plan_contrato'
        unique_together = (('plan_idplan', 'contrato_idcontrato', 'contrato_entidad_identidad'),)