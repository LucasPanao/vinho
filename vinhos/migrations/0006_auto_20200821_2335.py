# Generated by Django 3.1 on 2020-08-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinhos', '0005_auto_20200819_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinhos',
            name='codigo_barras_vinho',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vinhos',
            name='tipo_vinho',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
