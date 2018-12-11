# Generated by Django 2.1.3 on 2018-11-28 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lugares', '0005_auto_20181126_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoLocalidad',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=765)),
                ('notas', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='tipo_localidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lugares.TipoLocalidad'),
        ),
    ]
