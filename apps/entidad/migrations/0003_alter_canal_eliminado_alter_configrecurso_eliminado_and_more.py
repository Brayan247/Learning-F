# Generated by Django 4.1.1 on 2022-10-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0002_listanegra_eliminado_sucursal_eliminado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canal',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='configrecurso',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='emoticon',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='intencion',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='intenciontipo',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pagina',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recursosentidad',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='serviciosentidad',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='terminoscondiciones',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tipocanal',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
    ]
