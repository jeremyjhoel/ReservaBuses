# Generated by Django 4.2.1 on 2023-07-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disponibilidad',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='disponibilidad',
            name='horario',
            field=models.TimeField(),
        ),
    ]
