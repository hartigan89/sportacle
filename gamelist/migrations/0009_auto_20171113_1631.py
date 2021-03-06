# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamelist', '0008_delete_league'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'league',
                'verbose_name_plural': 'leagues',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='game',
            name='league',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gamelist.League'),
        ),
    ]
