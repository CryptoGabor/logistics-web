# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-14 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_auto_20180914_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wallettocca',
            options={'verbose_name': 'Wallet Assigned Crypto Address', 'verbose_name_plural': 'Wallet Assigned Crypto Addresses'},
        ),
    ]
