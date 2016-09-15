# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0007_teacher_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='fullName',
        ),
        migrations.AddField(
            model_name='teacher',
            name='slugName',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
