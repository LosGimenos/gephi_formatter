# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xl_formatter', '0003_auto_20170915_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagramdata',
            name='brand_source',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AddField(
            model_name='twitterdata',
            name='brand_source',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]