# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_article', '0002_auto_20180122_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(verbose_name=b'Cuerpo del Articulo'),
        ),
    ]
