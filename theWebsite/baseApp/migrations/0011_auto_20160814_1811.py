# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0010_auto_20160814_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='course',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
        migrations.AddField(
            model_name='attendance',
            name='courseDate',
            field=models.ForeignKey(to='baseApp.CourseDate', blank=True, related_name='attendance', null=True),
        ),
        migrations.AddField(
            model_name='coursedate',
            name='course',
            field=models.ForeignKey(to='baseApp.Course', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 14, 18, 11, 30, 255264, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 18, 11, 30, 255515, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 18, 11, 30, 255486, tzinfo=utc)),
        ),
    ]
