# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='ego',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='morphmodel',
            name='advantages',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='morphmodel',
            name='apt_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='morphmodel',
            name='disadvantages',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='morphmodel',
            name='implants',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='background',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='faction',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='morphmodel',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='psisleight',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
