# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0011_auto_20160814_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentPayment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('payment', models.ForeignKey(null=True, blank=True, to='baseApp.BookPayment')),
                ('student', models.ForeignKey(null=True, blank=True, to='baseApp.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='lisarsemester',
            name='bookPayment',
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 8, 14, 19, 46, 54, 824748, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='end',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 19, 46, 54, 824973, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='start',
            field=models.TimeField(default=datetime.datetime(2016, 8, 14, 19, 46, 54, 824941, tzinfo=utc)),
        ),
    ]
