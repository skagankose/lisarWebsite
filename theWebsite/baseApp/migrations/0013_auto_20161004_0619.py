# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0012_currentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lisarLevel',
            field=models.CharField(choices=[('1', '1'), ('2', '2')], max_length=10, verbose_name='Lisar Kademesi', default='1'),
        ),
        migrations.AlterField(
            model_name='student',
            name='schoolLevel',
            field=models.CharField(choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], max_length=10, verbose_name='Sınıf', default='9'),
        ),
    ]
