# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-05 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_slide',
            name='title',
            field=models.CharField(default=' ', max_length=1024),
        ),
    ]
