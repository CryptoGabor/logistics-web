# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0011_auto_20180914_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawrequest',
            name='freezedEur',
            field=models.FloatField(default=0.0, editable=False),
        ),
        migrations.AddField(
            model_name='withdrawrequest',
            name='freezedUsd',
            field=models.FloatField(default=0.0, editable=False),
        ),
        migrations.AlterField(
            model_name='wallettocca',
            name='assignedDate',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
