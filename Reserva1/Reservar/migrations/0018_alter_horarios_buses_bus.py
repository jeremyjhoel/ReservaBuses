# Generated by Django 4.2.1 on 2023-07-21 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0017_alter_reserva_fecha_alter_reserva_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horarios_buses',
            name='bus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Horarios_buses_bus', to='Reservar.bus'),
        ),
    ]