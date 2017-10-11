# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xl_formatter', '0002_instagramdata_instagrammention'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instagrammention',
            name='twitter_data',
        ),
        migrations.AddField(
            model_name='instagrammention',
            name='instagram_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='xl_formatter.InstagramData'),
        ),
    ]