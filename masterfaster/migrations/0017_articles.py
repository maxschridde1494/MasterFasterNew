# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-12 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('masterfaster', '0016_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=300)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterfaster.Topic')),
            ],
        ),
    ]
