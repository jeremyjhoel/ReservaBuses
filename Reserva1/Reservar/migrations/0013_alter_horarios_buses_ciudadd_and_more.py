# Generated by Django 4.2.1 on 2023-07-18 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0012_remove_disponibilidad_ruta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarios_buses',
            name='ciudadD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Horarios_buses_destino', to='Reservar.ciudades'),
        ),
        migrations.AlterField(
            model_name='horarios_buses',
            name='ciudadO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Horarios_buses_origen', to='Reservar.ciudades'),
        ),
    ]
