# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0006_auto_20160913_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='fullName',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
