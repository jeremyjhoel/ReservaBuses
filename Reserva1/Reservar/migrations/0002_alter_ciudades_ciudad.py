# Generated by Django 4.2.1 on 2023-06-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudades',
            name='ciudad',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
