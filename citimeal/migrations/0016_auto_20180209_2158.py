# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-09 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citimeal', '0015_cart_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.AddField(
            model_name='address',
            name='name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
