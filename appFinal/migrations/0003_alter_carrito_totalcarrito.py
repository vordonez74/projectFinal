# Generated by Django 3.2.5 on 2021-07-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFinal', '0002_auto_20210707_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='totalCarrito',
            field=models.FloatField(),
        ),
    ]
