# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-10 14:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_service_deliveryaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='deliveryAddress',
            new_name='profileAddress',
        ),
    ]
