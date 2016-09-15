# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0005_auto_20160913_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursedate',
            name='course',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses', blank=True, to='baseApp.Student'),
        ),
        migrations.DeleteModel(
            name='CourseDate',
        ),
    ]
