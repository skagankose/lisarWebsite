# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_auto_20160911_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='classroom',
            field=models.ForeignKey(null=True, related_name='course', to='baseApp.Classroom', blank=True),
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
    ]
