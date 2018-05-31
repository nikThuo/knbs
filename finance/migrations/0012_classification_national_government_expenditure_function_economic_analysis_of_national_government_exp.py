# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-07 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_classification_of_national_government_expenditure_by_function_economic_analysis_of_national_governme'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Classification_National_Government_Expenditure_Function',
        #     fields=[
        #         ('classification_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('government_function', models.CharField(max_length=100)),
        #         ('recurrent_account_in_millions', models.DecimalField(decimal_places=10, max_digits=65)),
        #         ('development_account_in_millions', models.DecimalField(decimal_places=10, max_digits=65)),
        #         ('total_in_millions', models.DecimalField(decimal_places=10, max_digits=65)),
        #         ('year', models.DateField()),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Economic_Analysis_Of_National_Government_Expenditure',
        #     fields=[
        #         ('expenditure_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('expenditure', models.CharField(max_length=100)),
        #         ('amount_in_millions', models.DecimalField(decimal_places=10, max_digits=65)),
        #         ('year', models.DateField()),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Economic_Classification_Of_County_Government_Expenditure',
        #     fields=[
        #         ('expenditure_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('county_government_expenditure', models.CharField(max_length=100)),
        #         ('amount_in_millions', models.DecimalField(decimal_places=10, max_digits=65)),
        #         ('year', models.DateField()),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='Statement_Of_National_Government_Operations',
        #     fields=[
        #         ('operation_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('national_government_operation', models.CharField(max_length=100)),
        #         ('amount_in_millions', models.DecimalField(decimal_places=10, max_digits=65)),
        #         ('year', models.DateField()),
        #     ],
        # ),
    ]
