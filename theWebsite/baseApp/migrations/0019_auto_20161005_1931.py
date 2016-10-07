# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0018_attendance_iscancelled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(related_name='classroom', to='baseApp.Student', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='classroom',
            field=models.ForeignKey(related_name='courses', to='baseApp.Classroom', blank=True, null=True),
        ),
    ]
