# Generated by Django 2.1.3 on 2018-11-14 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('fecha_inicio', models.IntegerField(blank=True, null=True)),
                ('fecha_final', models.IntegerField(blank=True, null=True)),
                ('notas', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=765)),
                ('genero', models.CharField(blank=True, max_length=765)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('fecha_defuncion', models.DateField(blank=True, null=True)),
                ('notas', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoOcupacion',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=765)),
                ('notas', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TituloOcupacion',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=765)),
                ('notas', models.TextField(blank=True)),
                ('tipo_ocupacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.TipoOcupacion')),
            ],
        ),
        migrations.AddField(
            model_name='ocupacion',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.Persona'),
        ),
        migrations.AddField(
            model_name='ocupacion',
            name='titulo_ocupacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.TituloOcupacion'),
        ),
    ]