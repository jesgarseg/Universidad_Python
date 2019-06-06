# Generated by Django 2.2.2 on 2019-06-06 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GestionAcademica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Creditos', models.PositiveSmallIntegerField()),
                ('Estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaMatricula', models.DateTimeField(auto_now_add=True)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.Alumno')),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GestionAcademica.Curso')),
            ],
        ),
    ]