# Generated by Django 4.1.1 on 2022-10-31 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_administrador_eliminado'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserEntidad',
        ),
    ]
