# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0019_auto_20161005_1931'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LisarSemester',
        ),
        migrations.DeleteModel(
            name='SchoolSemester',
        ),
    ]
