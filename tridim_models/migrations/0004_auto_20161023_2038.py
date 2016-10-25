# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-23 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tridim_models', '0003_auto_20161016_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedmodel',
            name='description',
            field=models.TextField(default='The user did not provide a description for this model.'),
        ),
        migrations.AddField(
            model_name='uploadedmodel',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
