# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-30 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('governance', '0016_persons_reported_tohave_committed_rape'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total_Prisoners_Committed_For_Debt_BySex',
            fields=[
                ('persons_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('proportion', models.DecimalField(decimal_places=1, max_digits=10)),
                ('gender', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
