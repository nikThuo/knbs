# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0006_current_use_of_contraception_by_county_distributionofoutpatientvisitsbytypeofhealthcareprovider_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiv_Aids_Awareness_And_Testing',
            fields=[
                ('awareness_id', models.AutoField(primary_key=True, serialize=False)),
                ('male', models.DecimalField(decimal_places=2, max_digits=10)),
                ('female', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hiv_awareness', models.CharField(max_length=100)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        # migrations.CreateModel(
        #     name='Registered_Active_Nhif_Members_By_County',
        #     fields=[
        #         ('member_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('formal', models.IntegerField()),
        #         ('informal', models.IntegerField()),
        #         ('year', models.IntegerField()),
        #         ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
        #     ],
        # ),
    ]
