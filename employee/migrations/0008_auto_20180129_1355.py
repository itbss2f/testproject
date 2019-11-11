# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2018-01-29 05:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20180129_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 247000)),
        ),
        migrations.AlterField(
            model_name='cities',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 250000)),
        ),
        migrations.AlterField(
            model_name='civil_status',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 255000)),
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 248000)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 241000)),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 248000)),
        ),
        migrations.AlterField(
            model_name='employmentrecord',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 246000)),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 258000)),
        ),
        migrations.AlterField(
            model_name='province',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 251000)),
        ),
        migrations.AlterField(
            model_name='region',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 251000)),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 249000)),
        ),
        migrations.AlterField(
            model_name='religion',
            name='date_entered',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 55, 15, 249000)),
        ),
    ]