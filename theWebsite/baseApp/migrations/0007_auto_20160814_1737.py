# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0006_auto_20160814_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpayment',
            name='month',
            field=models.CharField(blank=True, null=True, max_length=100, choices=[('eylül', 'Eylül'), ('ekim', 'Ekim'), ('kasım', 'Kasım'), ('aralık', 'Aralık'), ('ocak', 'Ocak'), ('şubat', 'Şubat'), ('mart', 'Mart'), ('nisan', 'Nisan'), ('mayıs', 'Mayıs'), ('haziran', 'Haziran'), ('temmuz', 'Temmuz'), ('ağustos', 'Ağustos')]),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 17, 37, 33, 339024, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 17, 37, 33, 338833, tzinfo=utc)),
        ),
    ]
