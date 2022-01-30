# Generated by Django 4.0.1 on 2022-01-30 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('reparacionID', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.TextField(max_length=100)),
                ('apellidos', models.TextField(max_length=100)),
                ('correo', models.CharField(max_length=40)),
                ('marca_modelo', models.TextField(max_length=100)),
                ('comentario', models.TextField(max_length=100)),
                ('esAceptada', models.BooleanField(default=False)),
            ],
        ),
    ]
