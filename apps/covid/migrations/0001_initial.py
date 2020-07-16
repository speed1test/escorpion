# Generated by Django 2.2.6 on 2020-07-16 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CuadroMedico',
            fields=[
                ('idCuadroMedico', models.AutoField(primary_key=True, serialize=False)),
                ('estado_paciente', models.BooleanField()),
                ('descripcion_paciente', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('idDepartamento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Minsal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('idMunicipio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_municipio', models.CharField(max_length=50)),
                ('departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='covid.Departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_paciente', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_paciente', models.CharField(blank=True, max_length=50, null=True)),
                ('dui_paciente', models.CharField(blank=True, max_length=9, null=True)),
                ('sexo_paciente', models.BooleanField()),
                ('fecha_paciente', models.DateTimeField()),
                ('localidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='covid.Municipio')),
            ],
        ),
    ]
