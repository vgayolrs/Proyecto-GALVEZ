# Generated by Django 2.1.3 on 2018-11-28 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0004_auto_20181128_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ['fecha_inicio', 'fecha_final']},
        ),
    ]
