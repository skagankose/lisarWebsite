# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0008_auto_20160814_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lisarsemester',
            name='courses',
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 14, 18, 2, 19, 562245, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 18, 2, 19, 562493, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 18, 2, 19, 562460, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='lisarsemester',
            name='bookPayment',
        ),
        migrations.AddField(
            model_name='lisarsemester',
            name='bookPayment',
            field=models.ManyToManyField(related_name='lisarsemester', null=True, blank=True, to='baseApp.BookPayment'),
        ),
    ]
