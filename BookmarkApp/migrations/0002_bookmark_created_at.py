# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookmarkApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='date created'),
        ),
    ]
