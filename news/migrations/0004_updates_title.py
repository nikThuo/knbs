# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170929_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates',
            name='title',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
