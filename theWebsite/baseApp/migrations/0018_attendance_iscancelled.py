# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0017_student_parentmailaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='isCancelled',
            field=models.BooleanField(default=False),
        ),
    ]
