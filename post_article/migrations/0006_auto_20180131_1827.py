# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-31 18:27
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_article', '0005_auto_20180131_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name=b'Cuerpo del Articulo'),
        ),
    ]
