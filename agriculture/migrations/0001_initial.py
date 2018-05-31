# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemical_Med_Feed_Input',
            fields=[
                ('chemical_med_feed_inputs_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=100)),
                ('cattle_feed', models.CharField(max_length=100)),
                ('dips_spray_fluids', models.CharField(max_length=100)),
                ('fungicides', models.CharField(max_length=100)),
                ('herbicides', models.CharField(max_length=100)),
                ('insecticides', models.CharField(max_length=100)),
                ('other_feeds', models.CharField(max_length=100)),
                ('other_livestock_drugs', models.CharField(max_length=100)),
                ('pig_feed', models.CharField(max_length=100)),
                ('plant_hormones', models.CharField(max_length=100)),
                ('poultry_feed', models.CharField(max_length=100)),
                ('vaccines', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cooperatives',
            fields=[
                ('cooperatives_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=100)),
                ('coffee', models.CharField(max_length=100)),
                ('cotton', models.CharField(max_length=100)),
                ('pyrethrum', models.CharField(max_length=100)),
                ('sugar', models.CharField(max_length=100)),
                ('dairy', models.CharField(max_length=100)),
                ('multi_purpose', models.CharField(max_length=100)),
                ('farm_purchase', models.CharField(max_length=100)),
                ('fisheries', models.CharField(max_length=100)),
                ('other_agricultural', models.CharField(max_length=100)),
                ('saccos', models.CharField(max_length=100)),
                ('consumer', models.CharField(max_length=100)),
                ('housing', models.CharField(max_length=100)),
                ('craftsmen', models.CharField(max_length=100)),
                ('transport', models.CharField(max_length=100)),
                ('other_non_agricultur', models.CharField(max_length=100)),
                ('unions', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gross_Market_Production',
            fields=[
                ('gross_market_production_at_constant_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=100)),
                ('cattle_and_calves_for_slaughter', models.CharField(max_length=100)),
                ('sugarcane', models.CharField(max_length=100)),
                ('vegetables', models.CharField(max_length=100)),
                ('cutflowers', models.CharField(max_length=100)),
                ('tea', models.CharField(max_length=100)),
                ('fruits', models.CharField(max_length=100)),
                ('poultry_and_eggs', models.CharField(max_length=100)),
                ('wheat', models.CharField(max_length=100)),
                ('sheep_goats_and_lambs_for_slaughter', models.CharField(max_length=100)),
                ('maize', models.CharField(max_length=100)),
                ('coffee', models.CharField(max_length=100)),
                ('barley', models.CharField(max_length=100)),
                ('dairy_products', models.CharField(max_length=100)),
                ('cotton', models.CharField(max_length=100)),
                ('hides_and_skins', models.CharField(max_length=100)),
                ('other_cereals', models.CharField(max_length=100)),
                ('other_temporary_crops', models.CharField(max_length=100)),
                ('pigs_for_slaughter', models.CharField(max_length=100)),
                ('wool', models.CharField(max_length=100)),
                ('potatoes', models.CharField(max_length=100)),
                ('pulses', models.CharField(max_length=100)),
                ('pyrethrum', models.CharField(max_length=100)),
                ('rice_paddy', models.CharField(max_length=100)),
                ('tobacco', models.CharField(max_length=100)),
                ('total_crops', models.CharField(max_length=100)),
                ('grand_total', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Irrigation_Schemes',
            fields=[
                ('irrigation_schemes_id', models.AutoField(primary_key=True, serialize=False)),
                ('ahero_gross_value_of_crop_millions', models.CharField(max_length=100)),
                ('ahero_hectares_cropped', models.CharField(max_length=100)),
                ('ahero_number_of_plots_holders', models.CharField(max_length=100)),
                ('ahero_paddy_yields_tonnes', models.CharField(max_length=100)),
                ('ahero_payments_to_plot_holders_millions', models.CharField(max_length=100)),
                ('all_schemes_gross_value_of_crop_millions', models.CharField(max_length=100)),
                ('all_schemes_hectares_cropped', models.CharField(max_length=100)),
                ('all_schemes_number_of_plots_holders', models.CharField(max_length=100)),
                ('all_schemes_paddy_yields_tonnes', models.CharField(max_length=100)),
                ('all_schemes_payments_to_plot_holders_millions', models.CharField(max_length=100)),
                ('bunyala_gross_value_of_crop_millions', models.CharField(max_length=100)),
                ('bunyala_hectares_cropped', models.CharField(max_length=100)),
                ('bunyala_number_of_plots_holders', models.CharField(max_length=100)),
                ('bunyala_paddy_yields_tonnes', models.CharField(max_length=100)),
                ('bunyala_payments_to_plot_holders_millions', models.CharField(max_length=100)),
                ('mwea_gross_value_of_crop_millions', models.CharField(max_length=100)),
                ('mwea_hectares_cropped', models.CharField(max_length=100)),
                ('mwea_number_of_plots_holders', models.CharField(max_length=100)),
                ('mwea_paddy_yields_tonnes', models.CharField(max_length=100)),
                ('mwea_payments_to_plot_holders_million', models.CharField(max_length=100)),
                ('perkerra_gross_value_of_crop_millions', models.CharField(max_length=100)),
                ('perkerra_hectares_cropped', models.CharField(max_length=100)),
                ('perkerra_number_of_plots_holders', models.CharField(max_length=100)),
                ('perkerra_payments_to_plot_holders_millions', models.CharField(max_length=100)),
                ('perkerra_seed_maize_tonnes', models.CharField(max_length=100)),
                ('west_kano_gross_value_of_crop_millions', models.CharField(max_length=100)),
                ('west_kano_hectares_cropped', models.CharField(max_length=100)),
                ('west_kano_number_of_plots_holders', models.CharField(max_length=100)),
                ('west_kano_paddy_yields_tonnes', models.CharField(max_length=100)),
                ('west_kano_payments_to_plot_holders_millions', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PriceToProducersForMeatMilk',
            fields=[
                ('price_to_producers_for_meat_milk_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=100)),
                ('beef_third_grade_per_kg', models.CharField(max_length=100)),
                ('pig_meat_per_kg', models.CharField(max_length=100)),
                ('whole_milk_per_litre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TotalShareCapital',
            fields=[
                ('total_share_capital_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=100)),
                ('coffee', models.CharField(max_length=100)),
                ('cotton', models.CharField(max_length=100)),
                ('pyrethrum', models.CharField(max_length=100)),
                ('sugar', models.CharField(max_length=100)),
                ('dairy', models.CharField(max_length=100)),
                ('multi_purpose', models.CharField(max_length=100)),
                ('farm_purchase', models.CharField(max_length=100)),
                ('fisheries', models.CharField(max_length=100)),
                ('other_agricultural', models.CharField(max_length=100)),
                ('total_agriculture', models.CharField(max_length=100)),
                ('saccos', models.CharField(max_length=100)),
                ('consumer', models.CharField(max_length=100)),
                ('housing', models.CharField(max_length=100)),
                ('craftsmen', models.CharField(max_length=100)),
                ('transport', models.CharField(max_length=100)),
                ('other_non_agricultural', models.CharField(max_length=100)),
                ('total_non_agricultural', models.CharField(max_length=100)),
                ('unions', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ValueOfAgriculturalInputs',
            fields=[
                ('value_of_agricultural_inputs_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('accounting_secretarial_and_auditing_services', models.IntegerField()),
                ('aerial_spraying', models.IntegerField()),
                ('artificial_insemination', models.IntegerField()),
                ('bags', models.CharField(max_length=100)),
                ('farm_planning_and_survey_services', models.CharField(max_length=100)),
                ('fertilizers', models.CharField(max_length=100)),
                ('fuel', models.CharField(max_length=100)),
                ('government_seed_inspection_services', models.CharField(max_length=100)),
                ('government_veterinary_inoculation_services', models.CharField(max_length=100)),
                ('insurance', models.CharField(max_length=100)),
                ('livestock_drugs_and_medicines', models.CharField(max_length=100)),
                ('manufactured_feeds', models.CharField(max_length=100)),
                ('marketing_research_and_publicity', models.CharField(max_length=100)),
                ('office_expenses', models.CharField(max_length=100)),
                ('other', models.CharField(max_length=100)),
                ('other_material_inputs', models.CharField(max_length=100)),
                ('other_agricultural_chemicals', models.CharField(max_length=100)),
                ('power', models.CharField(max_length=100)),
                ('private_veterinary_services', models.CharField(max_length=100)),
                ('seeds', models.CharField(max_length=100)),
                ('small_implements', models.CharField(max_length=100)),
                ('spares_and_maintenance_of_machinery', models.CharField(max_length=100)),
                ('tractor_services', models.CharField(max_length=100)),
                ('transportation', models.CharField(max_length=100)),
            ],
        ),
    ]
