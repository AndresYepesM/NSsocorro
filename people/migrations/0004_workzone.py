# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-14 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20180211_1708'),
    ]

    operations = [
        migrations.CreateModel(
            name='workzone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ct', models.CharField(max_length=20, verbose_name='Trabajo dentro de la parroquia')),
                ('des', models.TextField(max_length=150, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name_plural': 'Puesto de Trabajo',
                'ordering': ['ct'],
            },
        ),
    ]
