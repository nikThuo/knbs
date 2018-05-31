# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-31 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0014_distribution_sixthirteen_by_schooltype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribution_AboveFifteen_Ability_ReadWrite',
            fields=[
                ('distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('county_id', models.IntegerField()),
                ('literate', models.DecimalField(decimal_places=1, max_digits=10)),
                ('illiterate', models.DecimalField(decimal_places=1, max_digits=10)),
                ('not_stated', models.DecimalField(decimal_places=1, max_digits=10)),
                ('no_of_individuals', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]