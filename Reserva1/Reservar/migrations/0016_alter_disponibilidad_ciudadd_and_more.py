# Generated by Django 4.2.1 on 2023-07-18 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0015_alter_disponibilidad_ciudadd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidad',
            name='ciudadD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disponibilidades_destino', to='Reservar.ciudades'),
        ),
        migrations.AlterField(
            model_name='disponibilidad',
            name='ciudadO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disponibilidades_origen', to='Reservar.ciudades'),
        ),
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
        migrations.AlterField(
            model_name='reserva',
            name='ciudadD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas_destino', to='Reservar.ciudades'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='ciudadO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservas_origen', to='Reservar.ciudades'),
        ),
    ]