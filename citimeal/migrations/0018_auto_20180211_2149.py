# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citimeal', '0017_auto_20180211_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
