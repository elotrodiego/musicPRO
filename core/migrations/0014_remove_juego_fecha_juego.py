# Generated by Django 3.2.3 on 2021-06-16 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_juego_fecha_juego'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='fecha_juego',
        ),
    ]
