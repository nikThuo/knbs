# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-11 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_hospitalbedsandcots'),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentSecondarySchoolsByLevelAndSex',
            fields=[
                ('enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('boys', models.CharField(max_length=100)),
                ('girls', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Es_Educational_Institutions_Public_Tivet',
            fields=[
                ('institution_id', models.AutoField(primary_key=True, serialize=False)),
                ('institution', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_Educational_Institutions_Schools',
            fields=[
                ('institution_id', models.AutoField(primary_key=True, serialize=False)),
                ('institution', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_KcpeCandidatesAndMeanSubjectScore_Candidates',
            fields=[
                ('candidates_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_KcpeCandidatesAndMeanSubjectScore_Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('mean_score', models.DecimalField(decimal_places=2, max_digits=20)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_NationalGovtDevelopmentAndRecurrentExpenditure',
            fields=[
                ('expenditure_id', models.AutoField(primary_key=True, serialize=False)),
                ('expenditure', models.CharField(max_length=100)),
                ('expenditure_type', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_PrivateCandidatesRegisteredForKcpeBySex',
            fields=[
                ('kcpe_candidates_id', models.AutoField(primary_key=True, serialize=False)),
                ('proficiency', models.IntegerField()),
                ('kcpe', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Es_Public_Secondary_School_Trained_Teachers',
            fields=[
                ('teachers_id', models.AutoField(primary_key=True, serialize=False)),
                ('teachers', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_Public_Secondary_School_Untrained_Teachers',
            fields=[
                ('teachers_id', models.AutoField(primary_key=True, serialize=False)),
                ('teachers', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_Teacher_Trainees_Diploma_Enrolment',
            fields=[
                ('diploma_enrolment_id', models.AutoField(primary_key=True, serialize=False)),
                ('diploma_year', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_Teacher_Trainees_Private_Enrolment',
            fields=[
                ('private_enrolment_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Es_Teacher_Trainees_Public_Enrolment',
            fields=[
                ('public_enrolment_id', models.AutoField(primary_key=True, serialize=False)),
                ('primary_year', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]