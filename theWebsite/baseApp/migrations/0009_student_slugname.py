# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0008_auto_20160915_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slugName',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
