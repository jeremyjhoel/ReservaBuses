# Generated by Django 4.2.1 on 2023-07-18 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0013_alter_horarios_buses_ciudadd_and_more'),
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
    ]