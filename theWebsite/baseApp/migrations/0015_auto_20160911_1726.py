# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0014_auto_20160911_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='bookPayment',
        ),
        migrations.AddField(
            model_name='income',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='highschool',
            name='schoolType',
            field=models.CharField(blank=True, null=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='schoolSemester',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='SchoolSemester',
        ),
        migrations.DeleteModel(
            name='SchoolType',
        ),
    ]
