# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
