# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-30 06:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0020_auto_20180130_1429'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='year',
            new_name='yearfrom',
        ),
        migrations.AddField(
            model_name='college',
            name='yearto',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 803000)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 807000)),
        ),
        migrations.AlterField(
            model_name='civil_status',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 827000)),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 804000)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 797000)),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 804000)),
        ),
        migrations.AlterField(
            model_name='employmentrecord',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 802000)),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 830000)),
        ),
        migrations.AlterField(
            model_name='province',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 808000)),
        ),
        migrations.AlterField(
            model_name='region',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 808000)),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 805000)),
        ),
        migrations.AlterField(
            model_name='religion',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 14, 42, 5, 806000)),
        ),
    ]
