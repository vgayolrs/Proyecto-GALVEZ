# Generated by Django 2.1.3 on 2018-11-28 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0006_auto_20181127_2125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audiencia',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='jurisdiccion',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='localidad',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='provincia',
            options={'ordering': ['nombre']},
        ),
    ]
