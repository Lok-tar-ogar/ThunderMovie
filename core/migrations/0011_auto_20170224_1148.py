# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-24 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_film_if_useapi'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='download_link4',
            field=models.TextField(null=True, verbose_name='下载链接4-来自btbtdy.com'),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='download_link2',
            field=models.TextField(null=True, verbose_name='下载链接2-来自btbtdy.com'),
        ),
        migrations.AlterField(
            model_name='film',
            name='download_link',
            field=models.CharField(max_length=5000, null=True, verbose_name='下载链接-来自kanxi.cc'),
        ),
        migrations.AlterField(
            model_name='film',
            name='download_link2',
            field=models.CharField(max_length=500, null=True, verbose_name='下载链接2-来自ygdy8.net'),
        ),
    ]
