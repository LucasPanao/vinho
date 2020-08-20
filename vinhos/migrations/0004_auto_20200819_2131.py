# Generated by Django 3.1 on 2020-08-20 00:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinhos', '0003_auto_20200819_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinhos',
            name='data_cadastro',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 19, 21, 31, 27, 514393)),
        ),
        migrations.AlterField(
            model_name='vinhos',
            name='pais_vinho',
            field=models.CharField(choices=[('AR', 'Argentina'), ('AU', 'Austrália'), ('BR', 'Brasil'), ('CL', 'Chile'), ('DE', 'Alemanha'), ('ES', 'Espanha'), ('FR', 'França'), ('IT', 'Itália'), ('PT', 'Portugal'), ('US', 'Estados Unidos')], max_length=2),
        ),
    ]
