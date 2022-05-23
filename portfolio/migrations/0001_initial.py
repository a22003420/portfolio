# Generated by Django 4.0.4 on 2022-05-23 09:08

from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True)),
                ('foto', models.ImageField(upload_to=portfolio.models.resolution_path)),
            ],
        ),
        migrations.CreateModel(
            name='pontuacao_quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('pontuacao', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=20)),
                ('data', models.DateField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=20)),
                ('descricao', models.TextField()),
                ('link', models.URLField(blank=True, max_length=50, null=True)),
                ('docente_teorica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Cadeira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('ano', models.IntegerField(choices=[(1, '1º ano'), (2, '2º ano'), (3, '3º ano')], default='1')),
                ('titulo', models.CharField(max_length=50, unique=True)),
                ('descricao', models.TextField(max_length=300)),
                ('creditos', models.IntegerField(choices=[(4, '4 créditos'), (5, '5 créditos'), (6, '6 créditos'), (20, '20 créditos')], default='6')),
                ('semestre', models.PositiveSmallIntegerField(choices=[(1, '1º semestre'), (2, '2º semestre')], default='1')),
                ('competencias', models.ManyToManyField(to='portfolio.competencia')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.professor')),
            ],
        ),
    ]
