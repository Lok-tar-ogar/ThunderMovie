# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-09 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160902_1107'),
    ]

    operations = [

        migrations.AddField(
            model_name='film',
            name='download_link2',
            field=models.CharField(max_length=500, null=True, verbose_name='下载链接2'),
        ),
        migrations.AddField(
            model_name='film',
            name='download_link3',
            field=models.CharField(max_length=500, null=True, verbose_name='下载链接3'),
        ),

    ]
