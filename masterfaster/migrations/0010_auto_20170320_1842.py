# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterfaster', '0009_auto_20170320_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='same_as_billing',
            field=models.BooleanField(default=True),
        ),
    ]
