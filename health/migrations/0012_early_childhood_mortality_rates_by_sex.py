# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-08 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_months'),
    ]

    operations = [
        migrations.CreateModel(
            name='Early_Childhood_Mortality_Rates_By_Sex',
            fields=[
                ('rate_id', models.AutoField(primary_key=True, serialize=False)),
                ('mortality_rate', models.DecimalField(decimal_places=1, max_digits=10)),
                ('status', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
    ]
