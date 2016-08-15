# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0007_auto_20160814_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='date',
        ),
        migrations.RemoveField(
            model_name='coursedate',
            name='attendance',
        ),
        migrations.RemoveField(
            model_name='coursedate',
            name='day',
        ),
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(blank=True, to='baseApp.Course', related_name='attendance', null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.ForeignKey(blank=True, to='baseApp.CourseDate', related_name='attendance', null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(blank=True, to='baseApp.Student', related_name='attendance', null=True),
        ),
        migrations.AddField(
            model_name='coursedate',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 14, 17, 54, 49, 640219, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='courses',
        ),
        migrations.AddField(
            model_name='classroom',
            name='courses',
            field=models.ManyToManyField(related_name='classroom', blank=True, null=True, to='baseApp.Course'),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 17, 54, 49, 640449, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 17, 54, 49, 640419, tzinfo=utc)),
        ),
    ]
