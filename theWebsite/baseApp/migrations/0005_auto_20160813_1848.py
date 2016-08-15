# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0004_auto_20160813_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 8, 13, 18, 48, 19, 255126, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 8, 13, 18, 48, 19, 254904, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='student',
            name='bookPayment',
        ),
        migrations.AddField(
            model_name='student',
            name='bookPayment',
            field=models.ManyToManyField(to='baseApp.BookPayment', blank=True, null=True, related_name='students'),
        ),
    ]
