# Generated by Django 4.2.1 on 2023-07-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0003_remove_reserva_cantidadpasajes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=200),
        ),
    ]