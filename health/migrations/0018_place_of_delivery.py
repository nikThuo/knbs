# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-08 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0017_percentage_who_drink_alcohol_by_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place_Of_Delivery',
            fields=[
                ('place_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.DecimalField(decimal_places=1, max_digits=10)),
                ('place', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
    ]
