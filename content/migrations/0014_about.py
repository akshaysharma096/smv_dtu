# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-14 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_contact_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(blank=True, default=' ', max_length=1024)),
            ],
        ),
    ]