# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 21:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('deploys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploy',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 5, 10, 20, 59, 25, 105470, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deploy',
            name='modified',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 5, 10, 20, 59, 33, 121283, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
    ]
