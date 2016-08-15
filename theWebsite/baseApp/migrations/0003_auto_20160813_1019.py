# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 10:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0002_auto_20160806_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='LisarSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=300)),
                ('lastName', models.CharField(max_length=300)),
                ('phoneNumber', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.", regex='^\\+?1?\\d{12}$')])),
                ('mailAddress', models.EmailField(max_length=254)),
                ('university', models.CharField(max_length=300)),
                ('department', models.CharField(max_length=300)),
                ('role', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseApp.LisarSemester'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseApp.Teacher'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='courses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseApp.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classroom', to='baseApp.Classroom'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseApp.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='baseApp.LisarSemester'),
        ),
    ]
