# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governance', '0006_auto_20171109_1456'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Cases_Handled_By_Various_Courts',
        #     fields=[
        #         ('court_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('category', models.CharField(max_length=100)),
        #         ('kadhis_court', models.IntegerField()),
        #         ('magistrate_court', models.IntegerField()),
        #         ('high_court', models.IntegerField()),
        #         ('court_of_appeal', models.IntegerField()),
        #         ('supreme_court', models.IntegerField()),
        #         ('year', models.IntegerField()),
        #     ],
        # ),
        # migrations.AlterField(
        #     model_name='cases_handled_by_ethics_commision',
        #     name='year',
        #     field=models.CharField(max_length=100),
        # ),
    ]
