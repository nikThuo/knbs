# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 06:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Births_And_Deaths_By_Sex',
            fields=[
                ('count_id', models.AutoField(primary_key=True, serialize=False)),
                ('births', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Death_Causes',
            fields=[
                ('cause_id', models.AutoField(primary_key=True, serialize=False)),
                ('cause', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExpectedAndRegisteredBirthsAndDeaths',
            fields=[
                ('count_id', models.AutoField(primary_key=True, serialize=False)),
                ('coverage', models.CharField(max_length=100)),
                ('births', models.FloatField()),
                ('deaths', models.FloatField()),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        # migrations.CreateModel(
        #     name='Top_Ten_Death_Causes_2014',
        #     fields=[
        #         ('count_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('percent', models.FloatField()),
        #         ('total', models.IntegerField()),
        #         ('year', models.IntegerField()),
        #         ('cause_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vital_statistics.Death_Causes')),
        #         ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
        #     ],
        # ),
    ]
