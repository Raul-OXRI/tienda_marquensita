# Generated by Django 5.0.6 on 2024-06-07 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_client', models.CharField(max_length=100)),
                ('apellido_client', models.CharField(max_length=100)),
                ('correo_client', models.CharField(max_length=50)),
                ('telefono_client', models.CharField(max_length=13)),
                ('direccion_client', models.CharField(max_length=50)),
                ('fecha_registro_client', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=128)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
