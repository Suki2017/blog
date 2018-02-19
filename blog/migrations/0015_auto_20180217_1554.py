# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-17 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20180217_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='status',
            field=models.CharField(choices=[('正常', '正常'), ('代办', '代办'), ('正在处理', '正在处理'), ('已完成', '已完成'), ('已过期', '已过期')], max_length=16),
        ),
    ]
