# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-05 13:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20171002_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='info',
            name='avatar',
            field=models.CharField(blank=True, default='default', max_length=255, verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='info',
            name='college',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='毕业院校'),
        ),
        migrations.AlterField(
            model_name='info',
            name='sex',
            field=models.SmallIntegerField(choices=[(0, 'female'), (1, 'man'), (2, 'unknown')], default=1, verbose_name='性别'),
            preserve_default=False,
        ),
    ]
