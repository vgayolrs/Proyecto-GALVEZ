# Generated by Django 2.1.3 on 2018-11-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0005_actividad'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='fuente',
            field=models.CharField(blank=True, max_length=765),
        ),
    ]