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
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('isHere', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BookPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('month', models.CharField(blank=True, choices=[('eylül', 'Eylül'), ('ekim', 'Ekim'), ('kasım', 'Kasım'), ('aralık', 'Aralık'), ('ocak', 'Ocak'), ('şubat', 'Şubat'), ('mart', 'Mart'), ('nisan', 'Nisan'), ('mayıs', 'Mayıs'), ('haziran', 'Haziran'), ('temmuz', 'Temmuz'), ('ağustos', 'Ağustos')], max_length=100, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('totalAmount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.CharField(blank=True, null=True, max_length=300)),
                ('location', models.CharField(blank=True, null=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(blank=True, null=True, max_length=300)),
                ('start', models.TimeField(default=django.utils.timezone.now)),
                ('end', models.TimeField(default=django.utils.timezone.now)),
                ('classroom', models.ForeignKey(related_name='course', to='baseApp.Classroom', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('start', models.TimeField(default=django.utils.timezone.now)),
                ('end', models.TimeField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(to='baseApp.Course', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('grade', models.FloatField(blank=True, null=True)),
                ('course', models.ForeignKey(to='baseApp.Course', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(blank=True, null=True, max_length=500)),
                ('schoolType', models.CharField(blank=True, choices=[('Anadolu', 'Anadolu'), ('Fen', 'Fen'), ('İmam Hatip', 'İmam Hatip')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now, max_length=8)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LisarSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('semester', models.CharField(blank=True, null=True, max_length=300)),
                ('start', models.DateField(blank=True, null=True)),
                ('end', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(default=django.utils.timezone.now, max_length=8)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('semester', models.CharField(blank=True, null=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('firstName', models.CharField(verbose_name='İsim', max_length=300)),
                ('lastName', models.CharField(verbose_name='Soyisim', max_length=300)),
                ('phoneNumber', models.CharField(blank=True, verbose_name='Telefon', validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{12}$', message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")], max_length=13)),
                ('dateOfBirth', models.DateField(verbose_name='Doğum Tarihi', default=django.utils.timezone.now, max_length=8)),
                ('mailAddress', models.EmailField(verbose_name='Email Adresi', max_length=254)),
                ('adress', models.CharField(blank=True, verbose_name='Adres', null=True, max_length=500)),
                ('residence', models.CharField(blank=True, verbose_name='Kaldığı Yer', choices=[('Ev', 'Ev'), ('Yurt', 'Yurt')], max_length=10, null=True)),
                ('reference', models.TextField(blank=True, verbose_name='Referanslar', null=True)),
                ('admissionCause', models.TextField(blank=True, verbose_name='Başvuru Sebebi', null=True)),
                ('TEOGScore', models.FloatField(blank=True, verbose_name='TEOG Skoru', null=True)),
                ('schoolLevel', models.CharField(blank=True, verbose_name='Sınıf', choices=[('9.', '9.'), ('10.', '10.'), ('11.', '11.'), ('12.', '12.')], max_length=10, null=True)),
                ('lisarLevel', models.CharField(blank=True, verbose_name='Lisar Kademesi', choices=[('1.', '1.'), ('2.', '2.')], max_length=10, null=True)),
                ('profilePhoto', models.ImageField(blank=True, verbose_name='Fotoğraf', upload_to='img/')),
                ('highSchool', models.ForeignKey(related_name='students', to='baseApp.HighSchool', blank=True, verbose_name='Lise', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('isPaid', models.BooleanField(default=False)),
                ('payment', models.ForeignKey(to='baseApp.BookPayment', blank=True, null=True)),
                ('student', models.ForeignKey(to='baseApp.Student', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('firstName', models.CharField(blank=True, null=True, max_length=300)),
                ('lastName', models.CharField(blank=True, null=True, max_length=300)),
                ('phoneNumber', models.CharField(blank=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{12}$', message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.")], max_length=13)),
                ('mailAddress', models.EmailField(blank=True, null=True, max_length=254)),
                ('school', models.CharField(blank=True, null=True, max_length=300)),
                ('department', models.CharField(blank=True, null=True, max_length=300)),
                ('status', models.CharField(blank=True, choices=[('lisans', 'Lisans'), ('yüksek lisans', 'Yüksek Lisans'), ('doktora', 'Doktora')], max_length=30, null=True)),
                ('IBAN', models.CharField(blank=True, null=True, max_length=50)),
                ('profilePhoto', models.ImageField(blank=True, verbose_name='Fotoğraf', upload_to='img/')),
            ],
        ),
        migrations.AddField(
            model_name='coursegrade',
            name='student',
            field=models.ForeignKey(to='baseApp.Student', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(to='baseApp.Teacher', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='courseDate',
            field=models.ForeignKey(related_name='attendance', to='baseApp.CourseDate', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(related_name='attendance', to='baseApp.Student', blank=True, null=True),
        ),
    ]
