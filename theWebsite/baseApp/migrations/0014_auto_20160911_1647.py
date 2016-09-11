# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0013_auto_20160904_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='coursedate',
            name='end',
        ),
        migrations.RemoveField(
            model_name='coursedate',
            name='start',
        ),
        migrations.AddField(
            model_name='bookpayment',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='classroom',
            field=models.ForeignKey(to='baseApp.Classroom', related_name='course', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='end',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='course',
            name='start',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(to='baseApp.Teacher', related_name='course', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coursedate',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='bookPayment',
            field=models.ManyToManyField(blank=True, to='baseApp.BookPayment', related_name='students'),
        ),
    ]
