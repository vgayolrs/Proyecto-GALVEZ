# Generated by Django 2.1.3 on 2018-11-26 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0004_audiencia_enaudiencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enaudiencia',
            name='provincia',
        ),
        migrations.AddField(
            model_name='enaudiencia',
            name='audiencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lugares.Audiencia'),
        ),
    ]
