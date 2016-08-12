# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=500)),
                ('schoolType', models.ForeignKey(to='baseApp.SchoolType', null=True, blank=True, related_name='highSchools')),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='schoolName',
        ),
        migrations.AddField(
            model_name='student',
            name='highSchool',
            field=models.ForeignKey(to='baseApp.HighSchool', null=True, blank=True, related_name='students'),
        ),
    ]
