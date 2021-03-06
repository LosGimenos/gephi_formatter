# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xl_formatter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=140, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('author_gender', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=500, null=True)),
                ('sentiment', models.CharField(blank=True, max_length=300, null=True)),
                ('emotion', models.CharField(blank=True, max_length=300, null=True)),
                ('author_clout', models.IntegerField(blank=True, default=None, null=True)),
                ('contents', models.TextField(blank=True, null=True)),
                ('media_url_http', models.TextField(blank=True, null=True)),
                ('media_url_https', models.TextField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, default=None, null=True)),
                ('longitude', models.FloatField(blank=True, default=None, null=True)),
                ('followers', models.IntegerField(blank=True, default=None, null=True)),
                ('statuses', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstagramMention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=140, null=True)),
                ('mention', models.CharField(blank=True, max_length=200, null=True)),
                ('is_Direct', models.BooleanField(default=False)),
                ('is_Mixed', models.BooleanField(default=False)),
                ('twitter_data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='xl_formatter.TwitterData')),
            ],
        ),
    ]
