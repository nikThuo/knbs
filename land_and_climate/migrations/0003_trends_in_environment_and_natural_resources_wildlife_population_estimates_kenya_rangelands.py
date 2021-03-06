# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land_and_climate', '0002_environment_impact_assessments_by_sector_trendsinenvironmentandnaturalresourcesgrossvalueadded_wildl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trends_In_Environment_And_Natural_Resources',
            fields=[
                ('industry_id', models.AutoField(primary_key=True, serialize=False)),
                ('industry', models.CharField(max_length=100)),
                ('value_added', models.BigIntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wildlife_Population_Estimates_Kenya_Rangelands',
            fields=[
                ('species_id', models.AutoField(primary_key=True, serialize=False)),
                ('animal', models.CharField(max_length=100)),
                ('no_estimate', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
