# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0002_auto_20160810_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morph',
            name='effects',
            field=models.TextField(default='', null=True),
        ),
    ]
