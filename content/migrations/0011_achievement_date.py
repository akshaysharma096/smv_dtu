# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-07 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20170606_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='date',
            field=models.CharField(blank=True, default=' ', max_length=1024),
        ),
    ]