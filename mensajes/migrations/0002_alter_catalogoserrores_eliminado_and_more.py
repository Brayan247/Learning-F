# Generated by Django 4.1.1 on 2022-10-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogoserrores',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mensajeerrores',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
    ]