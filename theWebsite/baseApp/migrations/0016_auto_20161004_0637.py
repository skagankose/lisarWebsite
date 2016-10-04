# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0015_auto_20161004_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='lisarLevel',
            field=models.CharField(max_length=10, default='1', choices=[('1', '1'), ('2', '2'), ('3', 'Mezun')], verbose_name='Lisar Kademesi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='schoolLevel',
            field=models.CharField(max_length=10, default='9', choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', 'Mezun')], verbose_name='Sınıf'),
        ),
    ]
