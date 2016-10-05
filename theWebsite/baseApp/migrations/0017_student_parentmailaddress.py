# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0016_auto_20161004_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parentMailAddress',
            field=models.EmailField(verbose_name='Veli Email Adresi', default='2beordinary@gmail.com', max_length=254),
        ),
    ]
