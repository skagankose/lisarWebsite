# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('isHere', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BookPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('month', models.CharField(max_length=100, null=True, blank=True, choices=[('eylül', 'Eylül'), ('ekim', 'Ekim'), ('kasım', 'Kasım'), ('aralık', 'Aralık'), ('ocak', 'Ocak'), ('şubat', 'Şubat'), ('mart', 'Mart'), ('nisan', 'Nisan'), ('mayıs', 'Mayıs'), ('haziran', 'Haziran'), ('temmuz', 'Temmuz'), ('ağustos', 'Ağustos')])),
                ('cost', models.FloatField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('totalAmount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('code', models.CharField(max_length=300, null=True, blank=True)),
                ('location', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('start', models.TimeField(default=django.utils.timezone.now)),
                ('end', models.TimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(null=True, to='baseApp.Course', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseGrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('grade', models.FloatField(null=True, blank=True)),
                ('course', models.ForeignKey(null=True, to='baseApp.Course', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('schoolType', models.CharField(max_length=10, null=True, blank=True, choices=[('Anadolu', 'Anadolu'), ('Fen', 'Fen'), ('İmam Hatip', 'İmam Hatip')])),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField(max_length=8, default=django.utils.timezone.now)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LisarSemester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('semester', models.CharField(max_length=300, null=True, blank=True)),
                ('start', models.DateField(null=True, blank=True)),
                ('end', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date', models.DateField(max_length=8, default=django.utils.timezone.now)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSemester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('semester', models.CharField(max_length=300, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('firstName', models.CharField(verbose_name='İsim', max_length=300)),
                ('lastName', models.CharField(verbose_name='Soyisim', max_length=300)),
                ('phoneNumber', models.CharField(verbose_name='Telefon', max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.", regex='^\\+?1?\\d{12}$')], blank=True)),
                ('dateOfBirth', models.DateField(verbose_name='Doğum Tarihi', max_length=8, default=django.utils.timezone.now)),
                ('mailAddress', models.EmailField(verbose_name='Email Adresi', max_length=254)),
                ('adress', models.CharField(verbose_name='Adres', max_length=500, null=True, blank=True)),
                ('residence', models.CharField(verbose_name='Kaldığı Yer', max_length=10, null=True, blank=True, choices=[('ev', 'Ev'), ('yurt', 'Yurt')])),
                ('reference', models.TextField(verbose_name='Referanslar', null=True, blank=True)),
                ('Başvuru Sebebi', models.TextField(null=True, blank=True)),
                ('TEOGScore', models.FloatField(verbose_name='TEOG Skoru', null=True, blank=True)),
                ('schoolLevel', models.CharField(verbose_name='Sınıf', max_length=10, null=True, blank=True, choices=[('9.', '9.'), ('10.', '10.'), ('11.', '11.'), ('12.', '12.')])),
                ('lisarLevel', models.CharField(verbose_name='Lisar Kademesi', max_length=10, null=True, blank=True, choices=[('1.', '1.'), ('2.', '2.')])),
                ('profilePhoto', models.ImageField(verbose_name='Fotoğraf', blank=True, upload_to='img/')),
                ('highSchool', models.ForeignKey(null=True, to='baseApp.HighSchool', verbose_name='Lise', blank=True, related_name='students')),
            ],
        ),
        migrations.CreateModel(
            name='StudentPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('payment', models.ForeignKey(null=True, to='baseApp.BookPayment', blank=True)),
                ('student', models.ForeignKey(null=True, to='baseApp.Student', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('firstName', models.CharField(max_length=300, null=True, blank=True)),
                ('lastName', models.CharField(max_length=300, null=True, blank=True)),
                ('phoneNumber', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.", regex='^\\+?1?\\d{12}$')], blank=True)),
                ('mailAddress', models.EmailField(max_length=254, null=True, blank=True)),
                ('university', models.CharField(max_length=300, null=True, blank=True)),
                ('department', models.CharField(max_length=300, null=True, blank=True)),
                ('degree', models.CharField(max_length=30, null=True, blank=True, choices=[('lisans', 'Lisans'), ('yüksek lisans', 'Yüksek Lisans'), ('doktora', 'Doktora')])),
                ('ibanNo', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='student',
            field=models.ForeignKey(null=True, to='baseApp.Student', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, to='baseApp.Teacher', blank=True),
        ),
        migrations.AddField(
            model_name='classroom',
            name='courses',
            field=models.ManyToManyField(to='baseApp.Course', related_name='classroom', blank=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='courseDate',
            field=models.ForeignKey(null=True, to='baseApp.CourseDate', blank=True, related_name='attendance'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(null=True, to='baseApp.Student', blank=True, related_name='attendance'),
        ),
    ]
