# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0009_auto_20160814_1802'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='semester',
            new_name='lisarSemester',
        ),
        migrations.RemoveField(
            model_name='course',
            name='grade',
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='course',
            field=models.ForeignKey(to='baseApp.Course', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='student',
            field=models.ForeignKey(to='baseApp.Student', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 14, 18, 6, 32, 389909, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 18, 6, 32, 390130, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 18, 6, 32, 390103, tzinfo=utc)),
        ),
    ]
