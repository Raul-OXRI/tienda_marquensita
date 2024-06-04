# Generated by Django 5.0.6 on 2024-06-04 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre del producto')),
                ('descripcion_producto', models.CharField(blank=True, max_length=50, null=True, verbose_name='Descripción del producto')),
                ('precio_producto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio del producto')),
                ('stock_producto', models.IntegerField(blank=True, null=True, verbose_name='Cantidad del producto')),
                ('fecha_creacion_producto', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de ingreso del producto')),
                ('imagen_producto', models.ImageField(upload_to='productos_imagenes/', verbose_name='Imagen del producto')),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
