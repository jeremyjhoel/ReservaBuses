# Generated by Django 4.2.1 on 2023-07-05 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0006_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ruta',
            name='ciudadD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutas_destino', to='Reservar.ciudades', unique=True),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='ciudadO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutas_origen', to='Reservar.ciudades', unique=True),
        ),
    ]
