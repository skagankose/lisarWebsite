# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0010_auto_20160915_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='slugName',
        ),
        migrations.AddField(
            model_name='teacher',
            name='fullName',
            field=models.CharField(null=True, blank=True, max_length=300),
        ),
    ]
