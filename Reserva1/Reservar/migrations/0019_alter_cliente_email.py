# Generated by Django 4.2.1 on 2023-07-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0018_alter_horarios_buses_bus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
