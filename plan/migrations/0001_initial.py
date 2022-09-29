# Generated by Django 4.1.1 on 2022-09-29 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('idplan', models.AutoField(db_column='idPlan', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('acronimo', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=45)),
                ('costo', models.CharField(max_length=45)),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'plan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlanContrato',
            fields=[
                ('plan_idplan', models.IntegerField(db_column='plan_idPlan', primary_key=True, serialize=False)),
                ('contrato_idcontrato', models.IntegerField(db_column='contrato_idContrato')),
                ('contrato_entidad_identidad', models.IntegerField(db_column='contrato_entidad_idEntidad')),
            ],
            options={
                'db_table': 'plan_contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallePlan',
            fields=[
                ('plan_idplan', models.OneToOneField(db_column='plan_idPlan', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='plan.plan')),
                ('modulo_idmodulo', models.IntegerField(db_column='modulo_idModulo')),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'detalle_plan',
                'managed': False,
            },
        ),
    ]
