# Generated by Django 3.2.3 on 2021-06-16 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_juego_imagen_juego'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='carouse2',
            field=models.ImageField(default='static/core/img/default.png', upload_to='core', verbose_name='carousel2'),
        ),
        migrations.AddField(
            model_name='juego',
            name='carouse3',
            field=models.ImageField(default='static/core/img/default.png', upload_to='core', verbose_name='carousel3'),
        ),
        migrations.AddField(
            model_name='juego',
            name='carouse4',
            field=models.ImageField(default='static/core/img/default.png', upload_to='core', verbose_name='carousel4'),
        ),
        migrations.AddField(
            model_name='juego',
            name='carousel',
            field=models.ImageField(default='static/core/img/default.png', upload_to='core', verbose_name='carousel1'),
        ),
        migrations.AddField(
            model_name='juego',
            name='fecha_juego',
            field=models.DateField(default="2020-01-01", verbose_name='fecha de lanzamiento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='juego',
            name='precio_juego',
            field=models.IntegerField(verbose_name='precio del juego'),
        ),
    ]
