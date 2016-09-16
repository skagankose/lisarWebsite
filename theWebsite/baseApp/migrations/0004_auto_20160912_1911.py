# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0003_auto_20160912_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(null=True, blank=True, max_length=300, verbose_name='Bölüm', choices=[('bilgisayar mühendisliği', 'Bilgisayar Mühendisliği'), ('kimya', 'Kimya')]),
        ),
    ]
