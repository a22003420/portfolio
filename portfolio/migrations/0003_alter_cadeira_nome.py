# Generated by Django 4.0.4 on 2022-05-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_rename_professor_tecnologia_remove_pessoa_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]