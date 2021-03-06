# Generated by Django 3.1 on 2020-08-19 23:56

import datetime
import django.core.validators
from django.db import migrations, models
import vinhos.models


class Migration(migrations.Migration):

    dependencies = [
        ('vinhos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vinhos',
            old_name='nomeVinho',
            new_name='casta_vinho',
        ),
        migrations.RenameField(
            model_name='vinhos',
            old_name='descVinho',
            new_name='desc_vinho',
        ),
        migrations.RenameField(
            model_name='vinhos',
            old_name='imagemVinho',
            new_name='imagem_vinho',
        ),
        migrations.RemoveField(
            model_name='vinhos',
            name='dataCadastro',
        ),
        migrations.AddField(
            model_name='vinhos',
            name='ano_vinho',
            field=models.PositiveIntegerField(default=2020, validators=[django.core.validators.MinValueValidator(1600), vinhos.models.max_value_current_year]),
        ),
        migrations.AddField(
            model_name='vinhos',
            name='data_cadastro',
            field=models.DateTimeField(blank=True, default=datetime.date(2020, 8, 19)),
        ),
        migrations.AddField(
            model_name='vinhos',
            name='nome_vinho',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vinhos',
            name='pais_vinho',
            field=models.CharField(choices=[('AR', 'Argentina'), ('AU', 'Austrália'), ('BR', 'Brasil'), ('CL', 'Chile'), ('DE', 'Alemanha'), ('ES', 'Espanha'), ('FR', 'França'), ('IT', 'Itália'), ('US', 'Estados Unidos')], default='AR', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vinhos',
            name='produtor_vinho',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
