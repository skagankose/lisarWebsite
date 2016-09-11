# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Başvuru Sebebi',
        ),
        migrations.AddField(
            model_name='student',
            name='admissionCause',
            field=models.TextField(blank=True, null=True, verbose_name='Başvuru Sebebi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='residence',
            field=models.CharField(blank=True, choices=[('Ev', 'Ev'), ('Yurt', 'Yurt')], null=True, verbose_name='Kaldığı Yer', max_length=10),
        ),
    ]
