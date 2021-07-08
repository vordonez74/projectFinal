# Generated by Django 3.2.5 on 2021-07-07 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=64)),
                ('listaProductos', models.CharField(max_length=64)),
                ('totalCarrito', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('Imagen', models.CharField(max_length=64)),
                ('descripcion', models.CharField(max_length=64)),
                ('precio', models.CharField(max_length=64)),
                ('Categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catogory', to='appFinal.categorias')),
            ],
        ),
    ]
