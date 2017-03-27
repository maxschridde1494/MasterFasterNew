# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 22:08
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations
import sales.models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20170326_1813'),
    ]

    operations = [
        migrations.RemoveField(
        model_name='shoppingcart',
        name='items'
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), default=sales.models.ShoppingCart.default, size=None),
        ),
    ]
