# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0012_auto_20160814_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedate',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 9, 4, 15, 13, 15, 710847, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 9, 4, 15, 13, 15, 710911, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 9, 4, 15, 13, 15, 710885, tzinfo=utc)),
        ),
    ]
