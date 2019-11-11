# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-29 08:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20180129_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 719000)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 723000)),
        ),
        migrations.AlterField(
            model_name='civil_status',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 727000)),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 720000)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 713000)),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 720000)),
        ),
        migrations.AlterField(
            model_name='employmentrecord',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 718000)),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 730000)),
        ),
        migrations.AlterField(
            model_name='province',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 723000)),
        ),
        migrations.AlterField(
            model_name='region',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 724000)),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 721000)),
        ),
        migrations.AlterField(
            model_name='religion',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 16, 52, 47, 722000)),
        ),
        migrations.AlterModelTable(
            name='college',
            table='inq_college',
        ),
        migrations.AlterModelTable(
            name='primary',
            table='inq_primary',
        ),
        migrations.AlterModelTable(
            name='secondary',
            table='inq_secondary',
        ),
    ]