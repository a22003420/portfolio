# Generated by Django 4.0.4 on 2022-06-02 11:00

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_cadeira_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='TfcsDeisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=20)),
                ('orientador', models.CharField(max_length=20)),
                ('data', models.DateField(auto_now_add=True)),
                ('titulo', models.CharField(max_length=20)),
                ('resumo', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('relatorio', models.TextField()),
                ('imagem', models.ImageField(default='imagem.png', upload_to=portfolio.models.resolution_path)),
            ],
        ),
    ]
