# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-31 03:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterfaster', '0013_auto_20170324_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='same_as_billing',
        ),
    ]
