# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitpocket', '0002_auto_20170314_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='game_result',
            field=models.TextField(blank=True),
        ),
    ]