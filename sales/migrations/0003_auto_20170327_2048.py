# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20170327_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcart',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='size',
            field=models.CharField(max_length=100),
        ),
    ]
