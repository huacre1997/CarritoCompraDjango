# Generated by Django 3.0.6 on 2020-06-04 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20200602_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='ProdClasi',
            field=models.CharField(choices=[('TODOS', 'TODAS LAS EDADES'), ('TODOS+10', 'MAYORES DE 10 AÑOS'), ('ADOLESCENTES', 'MAYORES DE 13 AÑOS'), ('MADURO+17', 'MAYORES DE 17 AÑOS'), ('ADULTS+18', 'MAYORES DE 18 AÑOS'), ('SINCLASIFICAR', 'SIN CLASIFICAR')], max_length=20, verbose_name='Clasificación ESRB'),
        ),
    ]
