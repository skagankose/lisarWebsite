# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0021_auto_20161006_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highschool',
            name='schoolType',
            field=models.CharField(max_length=50, null=True, verbose_name='OKUL TİPİ', choices=[('Anadolu', 'Anadolu'), ('Fen', 'Fen'), ('İmam Hatip', 'İmam Hatip'), ('Anadolu İmam Hatip', 'Anadolu İmam Hatip')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='parentMailAddress',
            field=models.EmailField(max_length=254, blank=True, null=True, default='2beordinary@gmail.com', verbose_name='VELİ EMAIL ADRESİ'),
        ),
    ]
