# Generated by Django 4.2.1 on 2023-07-01 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0003_alter_disponibilidad_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidad',
            name='horario',
            field=models.TimeField(),
        ),
    ]