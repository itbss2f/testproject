# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-19 13:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_house_num', models.CharField(blank=True, max_length=64, null=True)),
                ('a_street_subd', models.CharField(blank=True, max_length=64, null=True)),
                ('a_barangay', models.CharField(blank=True, max_length=64, null=True)),
                ('p_house_num', models.CharField(blank=True, max_length=64, null=True)),
                ('p_street_subd', models.CharField(blank=True, max_length=64, null=True)),
                ('p_barangay', models.CharField(blank=True, max_length=64, null=True)),
                ('p_province', models.CharField(blank=True, max_length=64, null=True)),
                ('p_city', models.CharField(blank=True, max_length=64, null=True)),
                ('company_id', models.IntegerField(null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 497000))),
                ('date_modify', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_address',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=64)),
                ('company_id', models.IntegerField()),
                ('date_entered', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_branch',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('inter_level', models.CharField(max_length=64, null=True)),
                ('region', models.IntegerField(null=True)),
                ('province', models.IntegerField(null=True)),
                ('zip', models.IntegerField(null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 501000))),
                ('date_modify', models.DateField(null=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_cities',
            },
        ),
        migrations.CreateModel(
            name='Civil_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 505000))),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_civil_status',
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=100)),
                ('emp', models.CharField(max_length=100)),
                ('year', models.DateField(null=True)),
                ('address', models.CharField(max_length=100)),
                ('company_id', models.IntegerField(default=1)),
                ('date_entered', models.DateTimeField(null=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'educ_college',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=64)),
                ('date_entered', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_company',
            },
        ),
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfirst_name', models.CharField(blank=True, max_length=64, null=True)),
                ('cmiddle_name', models.CharField(blank=True, max_length=64, null=True)),
                ('clast_name', models.CharField(blank=True, max_length=64, null=True)),
                ('ctelnum', models.CharField(blank=True, max_length=64, null=True)),
                ('ccpnum', models.CharField(blank=True, max_length=64, null=True)),
                ('company_id', models.IntegerField(null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 499000))),
                ('date_modify', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_contactperson',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('company_id', models.IntegerField(default=1)),
                ('date_added', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=16, null=True)),
                ('code', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=64)),
                ('middle_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=128, null=True)),
                ('telnum', models.CharField(blank=True, max_length=32, null=True)),
                ('cphonenum', models.CharField(blank=True, max_length=32, null=True)),
                ('gender', models.IntegerField(null=True)),
                ('dob', models.DateTimeField(null=True)),
                ('pob', models.CharField(max_length=32, null=True)),
                ('designation', models.IntegerField(blank=True, null=True)),
                ('division', models.IntegerField(null=True)),
                ('date_hired', models.DateField(null=True)),
                ('date_resigned', models.DateTimeField(null=True)),
                ('cardno', models.IntegerField(blank=True, null=True)),
                ('sssno', models.CharField(blank=True, max_length=16, null=True)),
                ('tin', models.CharField(blank=True, max_length=16, null=True)),
                ('pagibig', models.CharField(blank=True, max_length=16, null=True)),
                ('philhealth', models.CharField(blank=True, max_length=16, null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 494000))),
                ('date_modify', models.DateTimeField(null=True)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Address')),
                ('branch_assigned', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Branch')),
                ('civil_status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.Civil_status')),
                ('company', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.Company')),
                ('contactperson', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.ContactPerson')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Department')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_employees',
            },
        ),
        migrations.CreateModel(
            name='EmployeeFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam_first_name', models.CharField(blank=True, max_length=64, null=True)),
                ('fam_middle_name', models.CharField(blank=True, max_length=64, null=True)),
                ('fam_last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('fam_gender', models.CharField(blank=True, max_length=64, null=True)),
                ('fam_relation', models.CharField(blank=True, max_length=64, null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 499000))),
                ('date_modify', models.DateTimeField(null=True)),
                ('f_emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_employee_family',
            },
        ),
        migrations.CreateModel(
            name='EmploymentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(blank=True, max_length=64, null=True)),
                ('yearfrom', models.DateTimeField(null=True)),
                ('yearto', models.DateTimeField(null=True)),
                ('company_id', models.IntegerField(null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 497000))),
                ('date_modify', models.DateTimeField(null=True)),
                ('is_deleted', models.IntegerField(default=0)),
                ('e_emp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_employment_record',
            },
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=64)),
                ('date_entered', models.DateTimeField(null=True)),
                ('has_late', models.IntegerField(default=1)),
                ('has_undertime', models.IntegerField(default=1)),
                ('has_overtime', models.IntegerField(default=1)),
                ('has_night_differential', models.IntegerField(default=1)),
                ('is_full_hours_worked', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_levels',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('country', models.CharField(max_length=64, null=True)),
                ('language', models.CharField(max_length=64, null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 508000))),
                ('date_modify', models.DateField(null=True)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_nationalities',
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=64)),
                ('date_added', models.DateTimeField(null=True)),
                ('company_id', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_positions',
            },
        ),
        migrations.CreateModel(
            name='Primary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=100)),
                ('emp', models.CharField(max_length=100)),
                ('year', models.DateField(null=True)),
                ('address', models.CharField(max_length=100)),
                ('company_id', models.IntegerField(default=1)),
                ('date_entered', models.DateTimeField(null=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'educ_primary',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=64, null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 502000))),
                ('date_modify', models.DateTimeField(null=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_province',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('code', models.CharField(blank=True, max_length=64, null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 502000))),
                ('date_modify', models.DateField(null=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_region',
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('date_entered', models.DateTimeField(default=datetime.datetime(2018, 1, 19, 21, 0, 41, 500000))),
                ('date_modify', models.DateTimeField(null=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_religion',
            },
        ),
        migrations.CreateModel(
            name='Secondary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=100)),
                ('emp', models.CharField(max_length=100)),
                ('year', models.DateField(null=True)),
                ('address', models.CharField(max_length=100)),
                ('company_id', models.IntegerField(default=1)),
                ('date_entered', models.DateTimeField(null=True)),
                ('is_deleted', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'educ_secondary',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=64)),
                ('active', models.IntegerField()),
                ('has_leave', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'inq_status',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_family',
            field=models.ManyToManyField(to='employee.EmployeeFamily'),
        ),
        migrations.AddField(
            model_name='employee',
            name='employment_record',
            field=models.ManyToManyField(to='employee.EmploymentRecord'),
        ),
        migrations.AddField(
            model_name='employee',
            name='nationality',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='employee.Nationality'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Positions'),
        ),
        migrations.AddField(
            model_name='employee',
            name='position_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Levels'),
        ),
        migrations.AddField(
            model_name='employee',
            name='religion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Religion'),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Status'),
        ),
        migrations.AddField(
            model_name='address',
            name='a_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Cities'),
        ),
        migrations.AddField(
            model_name='address',
            name='a_province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.Province'),
        ),
    ]
