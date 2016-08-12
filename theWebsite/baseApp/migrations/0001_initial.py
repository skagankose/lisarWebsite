# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('firstName', models.CharField(max_length=300)),
                ('lastName', models.CharField(max_length=300)),
                ('phoneNumber', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{12}$', message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")], blank=True)),
                ('mailAddress', models.EmailField(max_length=254)),
                ('schoolName', models.CharField(max_length=500, blank=True)),
                ('dateOfBirth', models.DateField(max_length=8, default=django.utils.timezone.now)),
            ],
        ),
    ]
