# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-02 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(default=1, max_length=88, verbose_name='姓名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='nickname',
            field=models.CharField(default=1, max_length=100, verbose_name='昵称'),
            preserve_default=False,
        ),
    ]