# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-31 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0015_distribution_abovefifteen_ability_readwrite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution_Three_Twentyfour_SchoolAttendance',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('county_id', models.IntegerField()),
                ('currently_attending', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_attending', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('age_group', models.CharField(max_length=10)),
            ],
        ),
    ]
