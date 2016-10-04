# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0013_auto_20161004_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lisarLevel',
            field=models.CharField(default='1', choices=[('1', '1'), ('2', '2'), ('Mezun', 'Mezun')], max_length=10, verbose_name='Lisar Kademesi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='schoolLevel',
            field=models.CharField(default='9', choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('Mezun', 'Mezun')], max_length=10, verbose_name='Sınıf'),
        ),
    ]
