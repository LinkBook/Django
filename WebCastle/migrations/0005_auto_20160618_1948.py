# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('WebCastle', '0004_auto_20160617_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_send',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 6, 18, 19, 48, 14, 778549),
                                       verbose_name='زمان ارسال'),
        ),
    ]
