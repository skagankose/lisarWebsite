# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_auto_20160912_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='schoolType',
            field=models.CharField(max_length=50, blank=True, null=True, choices=[('Lisesi', 'Lise'), ('Üniversitesi', 'Üniversite')]),
        ),
    ]
