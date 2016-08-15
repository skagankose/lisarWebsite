# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0005_auto_20160813_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='gpa',
            new_name='teogScore',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='role',
        ),
        migrations.AddField(
            model_name='student',
            name='place',
            field=models.CharField(null=True, choices=[('ev', 'Ev'), ('yurt', 'Yurt')], blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='reason',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='reference',
            field=models.CharField(null=True, blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='teacher',
            name='degree',
            field=models.CharField(null=True, choices=[('lisans', 'Lisans'), ('yüksek lisans', 'Yüksek Lisans'), ('doktora', 'Doktora')], blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='teacher',
            name='ibanNo',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 17, 29, 10, 915883, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 17, 29, 10, 915647, tzinfo=utc)),
        ),
    ]
