# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190318_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='content',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='design',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ratings',
            name='usability',
            field=models.IntegerField(default=0),
        ),
    ]
