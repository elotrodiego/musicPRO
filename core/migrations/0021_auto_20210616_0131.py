# Generated by Django 3.2.3 on 2021-06-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20210616_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juego',
            name='carousel',
            field=models.ImageField(default='/core/default.jpg', upload_to='core', verbose_name='carousel1'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='carousel2',
            field=models.ImageField(default='/core/default.jpg', upload_to='core', verbose_name='carousel2'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='carousel3',
            field=models.ImageField(default='/core/default.jpg', upload_to='core', verbose_name='carousel3'),
        ),
        migrations.AlterField(
            model_name='juego',
            name='carousel4',
            field=models.ImageField(default='/core/default.jpg', upload_to='core', verbose_name='carousel4'),
        ),
    ]
