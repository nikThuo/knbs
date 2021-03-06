# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('health', '0004_hospitalbedsandcots'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='Approved_Degree_Diploma_Programs',
        #     fields=[
        #         ('approved_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('year', models.CharField(max_length=100)),
        #         ('approved_degree_programmes', models.CharField(max_length=100)),
        #         ('approved_private_university_degreeprogrammes', models.CharField(max_length=100)),
        #         ('validated_diploma_programmes', models.CharField(max_length=100)),
        #     ],
        # ),
        migrations.CreateModel(
            name='Csa_AdultEducationCentresBySubCounty',
            fields=[
                ('adult_centre_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('centres', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_AdultEducationEnrolmentBySexAndSubcounty',
            fields=[
                ('adult_enrolment_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('number', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_AdultEducationProficiencyTestResults',
            fields=[
                ('adult_proficiency_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('no_sat', models.IntegerField()),
                ('no_passed', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_EcdeCentresByCategoryAndSubCounty',
            fields=[
                ('ecde_centre_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('no_of_centres', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_PrimaryEnrolmentAndAccessIndicators',
            fields=[
                ('primary_enrolment_id', models.AutoField(primary_key=True, serialize=False)),
                ('enrolment', models.IntegerField()),
                ('ger', models.FloatField()),
                ('ner', models.FloatField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_PrimarySchoolEnrollmentByClassSexAndSubCounty',
            fields=[
                ('primary_enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('class_1', models.IntegerField()),
                ('class_2', models.IntegerField()),
                ('class_3', models.IntegerField()),
                ('class_4', models.IntegerField()),
                ('class_5', models.IntegerField()),
                ('class_6', models.IntegerField()),
                ('class_7', models.IntegerField()),
                ('class_8', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_PrimarySchoolsByCategoryAndSubCounty',
            fields=[
                ('primary_schools_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('no_of_schools', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_SecondaryEnrolmentAndAccessIndicators',
            fields=[
                ('secondary_enrolment_id', models.AutoField(primary_key=True, serialize=False)),
                ('enrolment', models.IntegerField()),
                ('ger', models.FloatField()),
                ('ner', models.FloatField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_SecondarySchoolEnrollmentByClassSexSubCounty',
            fields=[
                ('enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('form_1', models.IntegerField()),
                ('form_2', models.IntegerField()),
                ('form_3', models.IntegerField()),
                ('form_4', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_SecondarySchoolsByCategoryAndSubCounty',
            fields=[
                ('sec_schools_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('no_of_schools', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_StudentEnrolmentInYouthPolytechnics',
            fields=[
                ('youth_poly_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('institution_name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('male', models.IntegerField()),
                ('female', models.IntegerField()),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_TeacherTrainingColleges',
            fields=[
                ('teacher_colleges_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('pre_primary', models.IntegerField()),
                ('primary_sc', models.IntegerField()),
                ('secondary', models.IntegerField()),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='Csa_YouthPolytechnicsByCategoryAndSubCounty',
            fields=[
                ('youth_poly_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_county_id', models.IntegerField()),
                ('public', models.IntegerField()),
                ('private', models.IntegerField()),
                ('year', models.IntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
        migrations.CreateModel(
            name='NationalTrendsKcseCandidatesMeanGradebySex',
            fields=[
                ('national_trends_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('a_plain', models.CharField(max_length=100)),
                ('a_minus', models.CharField(max_length=100)),
                ('b_plus', models.CharField(max_length=100)),
                ('b_plain', models.CharField(max_length=100)),
                ('b_minus', models.CharField(max_length=100)),
                ('c_plus', models.CharField(max_length=100)),
                ('c_plain', models.CharField(max_length=100)),
                ('c_minus', models.CharField(max_length=100)),
                ('d_plus', models.CharField(max_length=100)),
                ('d_plain', models.CharField(max_length=100)),
                ('d_minus', models.CharField(max_length=100)),
                ('e_plain', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Number_Educational_Institutions',
            fields=[
                ('educational_institutions_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=100)),
                ('schools_primary_secondary', models.CharField(max_length=100)),
                ('teacher_training_colleges', models.CharField(max_length=100)),
                ('tivet_institutions', models.CharField(max_length=100)),
                ('universities', models.CharField(max_length=100)),
            ],
        ),
        # migrations.CreateModel(
        #     name='StudentEnrollmentBySexTechnicalInstitutions',
        #     fields=[
        #         ('student_enrollment_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('institution', models.CharField(max_length=100)),
        #         ('year', models.CharField(max_length=100)),
        #         ('male', models.CharField(max_length=100)),
        #         ('female', models.CharField(max_length=100)),
        #     ],
        # ),
        # migrations.CreateModel(
        #     name='StudentEnrollmentPublicUniversities',
        #     fields=[
        #         ('student_enrollment_id', models.AutoField(primary_key=True, serialize=False)),
        #         ('year', models.CharField(max_length=100)),
        #         ('undergraduates', models.CharField(max_length=100)),
        #         ('postgraduates', models.CharField(max_length=100)),
        #         ('other', models.CharField(max_length=100)),
        #     ],
        # ),
        migrations.CreateModel(
            name='TotalSecondarySchoolEnrollmentByYear',
            fields=[
                ('school_enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=100)),
                ('number_of_students', models.CharField(max_length=100)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.Counties')),
            ],
        ),
    ]
