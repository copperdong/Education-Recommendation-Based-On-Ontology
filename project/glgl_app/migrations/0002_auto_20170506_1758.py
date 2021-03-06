# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glgl_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='dummy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='video',
            name='cover',
            field=models.ImageField(default='default/default_headimage.jpg', upload_to='covers'),
        ),
    ]
