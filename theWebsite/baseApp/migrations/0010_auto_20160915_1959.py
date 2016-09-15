# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0009_student_slugname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='slugName',
        ),
        migrations.AddField(
            model_name='student',
            name='fullName',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
    ]
