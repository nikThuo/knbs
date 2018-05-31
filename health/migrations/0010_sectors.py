# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_registered_active_nhif_members_by_county_registered_active_nhif_members_nationally'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('sector_id', models.AutoField(primary_key=True, serialize=False)),
                ('sector_name', models.CharField(max_length=100)),
                ('report', models.CharField(max_length=100)),
                ('coverage', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('table_name', models.CharField(max_length=100)),
                ('api_url', models.CharField(max_length=100)),
                ('embed_script', models.TextField()),
            ],
        ),
    ]