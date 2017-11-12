# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-20 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0003_game_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='outcome',
            field=models.CharField(choices=[('U', 'Unknown'), ('V', 'Visitor'), ('H', 'Home')], max_length=1),
        ),
    ]
