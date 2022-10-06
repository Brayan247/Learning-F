# Generated by Django 4.1.1 on 2022-10-06 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entidad', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEntidad',
            fields=[
                ('id_user_entidad', models.AutoField(db_column='id_user_entidad', primary_key=True, serialize=False)),
                ('id_entidad', models.ForeignKey(db_column='id_entidad', on_delete=django.db.models.deletion.DO_NOTHING, to='entidad.entidad')),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_entidad',
                'managed': True,
                'unique_together': {('id_user',)},
            },
        ),
        migrations.DeleteModel(
            name='LogsSystemFintech',
        ),
    ]