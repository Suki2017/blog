# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-06 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_friendlink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('site', models.URLField(help_text='站点主页')),
            ],
            options={
                'verbose_name': '社交网站',
                'verbose_name_plural': '社交网站',
                'db_table': 'contacts',
            },
        ),
    ]
