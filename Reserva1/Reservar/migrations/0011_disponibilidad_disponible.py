# Generated by Django 4.2.1 on 2023-07-18 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0010_remove_disponibilidad_disponible_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='disponibilidad',
            name='disponible',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]