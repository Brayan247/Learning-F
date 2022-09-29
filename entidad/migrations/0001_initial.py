# Generated by Django 4.1.1 on 2022-09-29 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('idcanal', models.AutoField(db_column='idCanal', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=55)),
                ('credenciales', models.TextField(db_collation='utf8mb4_bin')),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'canal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ConfigRecurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=45)),
                ('valor', models.TextField()),
                ('type', models.CharField(max_length=45)),
                ('descripcion', models.TextField()),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'config_recurso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('idcontrato', models.AutoField(db_column='idContrato', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('acronimo', models.CharField(max_length=45)),
                ('duracion', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('clausulas', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emoticon',
            fields=[
                ('idemoticon', models.AutoField(db_column='idEmoticon', primary_key=True, serialize=False)),
                ('emoticon', models.ImageField(upload_to='')),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('codigo', models.CharField(blank=True, max_length=2, null=True)),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'emoticon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('identidad', models.AutoField(db_column='idEntidad', primary_key=True, serialize=False)),
                ('titulo_pagina', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('logo_horizontal', models.ImageField(upload_to='')),
                ('logo_vertical', models.ImageField(upload_to='')),
                ('color_primario', models.CharField(max_length=45)),
                ('color_secundario', models.CharField(max_length=45)),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='')),
                ('direccion', models.CharField(blank=True, max_length=400, null=True)),
                ('copyright', models.URLField(blank=True, max_length=400, null=True)),
                ('contacto', models.CharField(blank=True, max_length=45, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('lema', models.CharField(blank=True, max_length=45, null=True)),
                ('facebook', models.URLField(blank=True, max_length=45, null=True)),
                ('twitter', models.URLField(blank=True, max_length=45, null=True)),
                ('activo_bot', models.IntegerField(blank=True, null=True)),
                ('tiempo_respuesta_bot', models.IntegerField(blank=True, null=True)),
                ('nro_intentos_fallidos', models.IntegerField(blank=True, null=True)),
                ('tiempo_bloqueo', models.IntegerField(blank=True, null=True)),
                ('ip_produccion', models.CharField(blank=True, max_length=100, null=True)),
                ('ip_dev', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
                ('respaldocliente', models.IntegerField()),
                ('tiempo_espera_code', models.IntegerField()),
                ('plantilla', models.IntegerField()),
            ],
            options={
                'db_table': 'entidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Intencion',
            fields=[
                ('idintencion', models.AutoField(db_column='idIntencion', primary_key=True, serialize=False)),
                ('intencion', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('respuesta', models.TextField(blank=True, db_collation='utf8mb4_bin', null=True)),
                ('multi_mensaje', models.IntegerField(blank=True, null=True)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('mensajedialogflow', models.TextField(blank=True, db_column='mensajeDialogflow', null=True)),
                ('eliminado', models.IntegerField()),
                ('fecha_registro', models.DateTimeField()),
                ('fecha_actualizacion', models.DateTimeField()),
                ('idtipointencion', models.IntegerField(db_column='idTipoIntencion')),
                ('idrecursos', models.IntegerField(db_column='idRecursos')),
                ('identidad', models.IntegerField(db_column='idEntidad')),
            ],
            options={
                'db_table': 'intencion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IntencionTipo',
            fields=[
                ('idtipointencion', models.AutoField(db_column='idTipoIntencion', primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=45)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'intencion_tipo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ListaNegra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField()),
                ('fecha_actualizacion', models.DateTimeField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('intentos_actuales', models.IntegerField()),
                ('intentos_totales', models.IntegerField()),
                ('estado', models.IntegerField()),
            ],
            options={
                'db_table': 'lista_negra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('idpagina', models.AutoField(db_column='idPagina', primary_key=True, serialize=False)),
                ('identidad', models.IntegerField(db_column='idEntidad')),
                ('nombre', models.CharField(max_length=45)),
                ('clave', models.CharField(max_length=60)),
                ('token', models.CharField(max_length=200)),
                ('version', models.IntegerField()),
                ('idfacebook', models.CharField(db_column='idFacebook', max_length=45)),
                ('versionfacebook', models.CharField(db_column='versionFacebook', max_length=3)),
                ('eliminado', models.IntegerField()),
                ('fecha_registro', models.DateTimeField()),
                ('fecha_actualizacion', models.DateTimeField()),
            ],
            options={
                'db_table': 'pagina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RecursosEntidad',
            fields=[
                ('idrecursos', models.AutoField(db_column='idRecursos', primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=45)),
                ('tipo', models.CharField(max_length=45)),
                ('param_entrada', models.TextField(blank=True, db_collation='utf8mb4_bin', null=True)),
                ('param_salida', models.TextField(blank=True, db_collation='utf8mb4_bin', null=True)),
                ('fecha_actualizacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
                ('id_entidad', models.IntegerField()),
                ('id_modulo', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'recursos_entidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=250)),
                ('icono', models.CharField(max_length=45)),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiciosEntidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField()),
                ('fecha_actualizacion', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
                ('id_servicio', models.IntegerField()),
                ('id_entidad', models.IntegerField()),
            ],
            options={
                'db_table': 'servicios_entidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('referencia', models.CharField(max_length=200)),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('tipo', models.CharField(max_length=45)),
                ('estado', models.IntegerField()),
                ('id_entidad', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TerminosCondiciones',
            fields=[
                ('idtermino', models.AutoField(db_column='idTermino', primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=550)),
                ('descripcion', models.TextField()),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
                ('entidad_identidad', models.IntegerField(db_column='entidad_idEntidad')),
            ],
            options={
                'db_table': 'terminos_condiciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoCanal',
            fields=[
                ('idtipocanal', models.AutoField(db_column='idTipoCanal', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=55)),
                ('descripcion', models.CharField(blank=True, max_length=55, null=True)),
                ('fecha_actualizacion', models.DateTimeField()),
                ('fecha_registro', models.DateTimeField()),
                ('eliminado', models.IntegerField()),
            ],
            options={
                'db_table': 'tipo_canal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CamposPersonalizadosEntidad',
            fields=[
                ('entidad_identidad', models.OneToOneField(db_column='entidad_idEntidad', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='entidad.entidad')),
                ('habilitado', models.IntegerField()),
            ],
            options={
                'db_table': 'campos_personalizados_entidad',
                'managed': False,
            },
        ),
    ]
