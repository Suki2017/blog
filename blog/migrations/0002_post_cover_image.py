# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-02 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover_image',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]