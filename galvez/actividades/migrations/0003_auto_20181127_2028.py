# Generated by Django 2.1.3 on 2018-11-28 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0005_auto_20181126_0944'),
        ('actividades', '0002_cargo_jurisdiccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cargo',
            name='provincia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lugares.Provincia'),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='jurisdiccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lugares.Jurisdiccion'),
        ),
    ]
