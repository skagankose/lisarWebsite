# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0003_auto_20160813_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('isHere', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BookPayment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('month', models.CharField(null=True, max_length=100, blank=True)),
                ('cost', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('totalAmount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CourseDate',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('day', models.CharField(max_length=300)),
                ('start', models.TimeField(default=datetime.datetime(2016, 8, 13, 18, 32, 42, 996176, tzinfo=utc))),
                ('end', models.TimeField(default=datetime.datetime(2016, 8, 13, 18, 32, 42, 996441, tzinfo=utc))),
                ('attendance', models.ForeignKey(null=True, to='baseApp.Attendance', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseGrade',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('grade', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField(default=django.utils.timezone.now, max_length=8)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField(default=django.utils.timezone.now, max_length=8)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSemester',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('semester', models.CharField(null=True, max_length=300, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AddField(
            model_name='lisarsemester',
            name='courses',
            field=models.ForeignKey(null=True, related_name='lisarsemester', to='baseApp.Course', blank=True),
        ),
        migrations.AddField(
            model_name='lisarsemester',
            name='semester',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='adress',
            field=models.CharField(null=True, max_length=500, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gpa',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='code',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='courses',
            field=models.ForeignKey(null=True, related_name='classroom', to='baseApp.Course', blank=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='location',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='highschool',
            name='name',
            field=models.CharField(null=True, max_length=500, blank=True),
        ),
        migrations.AlterField(
            model_name='lisarsemester',
            name='end',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='lisarsemester',
            name='start',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.ForeignKey(null=True, related_name='students', to='baseApp.Classroom', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.ForeignKey(null=True, related_name='students', to='baseApp.LisarSemester', blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='firstName',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='lastName',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mailAddress',
            field=models.EmailField(null=True, max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='role',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='university',
            field=models.CharField(null=True, max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='date',
            field=models.ForeignKey(null=True, related_name='course', to='baseApp.CourseDate', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='grade',
            field=models.ForeignKey(null=True, related_name='course', to='baseApp.CourseGrade', blank=True),
        ),
        migrations.AddField(
            model_name='lisarsemester',
            name='bookPayment',
            field=models.ForeignKey(null=True, related_name='lisarsemester', to='baseApp.BookPayment', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='bookPayment',
            field=models.ForeignKey(null=True, related_name='students', to='baseApp.BookPayment', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='schoolSemester',
            field=models.ForeignKey(null=True, related_name='students', to='baseApp.SchoolSemester', blank=True),
        ),
    ]
