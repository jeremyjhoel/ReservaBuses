# Generated by Django 4.2.1 on 2023-07-17 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0006_alter_cliente_rut'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='ruta',
        ),
        migrations.AddField(
            model_name='reserva',
            name='ciudadD',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reservas_destino', to='Reservar.ruta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='ciudadO',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reservas_origen', to='Reservar.ruta'),
            preserve_default=False,
        ),
    ]
