# Generated by Django 3.2.3 on 2021-06-16 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_juego_fecha_juego'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='carousel',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='carousel2',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='carousel3',
        ),
        migrations.RemoveField(
            model_name='juego',
            name='carousel4',
        ),
    ]
