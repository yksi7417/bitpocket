# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitpocket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='num_of_games_played',
            field=models.IntegerField(default=0),
        ),
    ]
