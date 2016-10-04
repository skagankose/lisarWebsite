# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0014_auto_20161004_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lisarLevel',
            field=models.CharField(default='1', verbose_name='Lisar Kademesi', max_length=10, choices=[('1', '1'), ('2', '2'), ('a', 'Mezun')]),
        ),
    ]
