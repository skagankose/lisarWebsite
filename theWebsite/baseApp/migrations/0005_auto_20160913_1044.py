# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0004_auto_20160912_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateAttendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now, max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='courseDate',
        ),
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(blank=True, related_name='attendance', null=True, to='baseApp.Course'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, max_length=8),
        ),
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(null=True, blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='course',
            name='lisarLevel',
            field=models.CharField(null=True, blank=True, choices=[('1.', '1.'), ('2.', '2.')], max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='isHere',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='classroom',
            field=models.CharField(null=True, blank=True, choices=[('A130', 'A130'), ('B240', 'B240'), ('C350', 'C350')], max_length=30),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='IBAN',
            field=models.CharField(verbose_name='IBAN', null=True, validators=[django.core.validators.RegexValidator(message="IBAN must be entered in the format: 'TR999999999999999999999999'. 24 digits allowed.", regex='^\\w{2}\\d{24}$')], blank=True, max_length=26),
        ),
        migrations.AddField(
            model_name='createattendance',
            name='course',
            field=models.ForeignKey(blank=True, null=True, to='baseApp.Course'),
        ),
    ]
