# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-08 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthFacilitiesByOwnershipOfHealthFacilities',
            fields=[
                ('facility_ownership_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_facilities', models.IntegerField()),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='HealthFacilitiesByOwnershipOfHealthFacilities_Ids',
            fields=[
                ('health_facility_id', models.AutoField(primary_key=True, serialize=False)),
                ('health_facility', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredMedicalPersonnel',
            fields=[
                ('registered_medical_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_personnel', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='RegisteredMedicalPersonnel_Ids',
            fields=[
                ('medical_personnel_id', models.AutoField(primary_key=True, serialize=False)),
                ('medical_personnel', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='registeredmedicalpersonnel',
            name='medical_personnel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.RegisteredMedicalPersonnel_Ids'),
        ),
        migrations.AddField(
            model_name='healthfacilitiesbyownershipofhealthfacilities',
            name='health_facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.HealthFacilitiesByOwnershipOfHealthFacilities_Ids'),
        ),
    ]
