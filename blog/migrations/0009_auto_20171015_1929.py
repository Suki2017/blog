# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-15 11:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_contact_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('praises', models.IntegerField(default=0, help_text='点赞数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='info',
            name='role',
        ),
        migrations.RemoveField(
            model_name='info',
            name='temp_role',
        ),
        migrations.RemoveField(
            model_name='info',
            name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='thanks',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Info',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='blog.Post'),
        ),
    ]
