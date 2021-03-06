# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-27 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_number_of_candidates_by_sex_in_kcse'),
    ]

    operations = [
        migrations.CreateModel(
            name='primary_school_enrolments_by_sex',
            fields=[
                ('enrolment_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('boys', models.IntegerField()),
                ('girls', models.IntegerField()),
                ('total', models.IntegerField()),
                ('percentage_girls', models.DecimalField(decimal_places=1, max_digits=10)),
                ('parity_index', models.DecimalField(decimal_places=1, max_digits=10)),
            ],
        ),
    ]
