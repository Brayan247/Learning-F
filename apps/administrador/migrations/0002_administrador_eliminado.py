# Generated by Django 4.1.1 on 2022-10-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='eliminado',
            field=models.IntegerField(default=0),
        ),
    ]
