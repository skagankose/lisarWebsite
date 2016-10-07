# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0020_auto_20161006_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='fullName',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='fullName',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='course',
            field=models.ForeignKey(related_name='attendance', to='baseApp.Course', null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(related_name='attendance', verbose_name='ÖĞRENCİ', to='baseApp.Student', null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='code',
            field=models.CharField(verbose_name='KOD', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='location',
            field=models.CharField(blank=True, verbose_name='YER', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(blank=True, verbose_name='ÖĞRENCİLER', related_name='classroom', to='baseApp.Student'),
        ),
        migrations.AlterField(
            model_name='course',
            name='classroom',
            field=models.ForeignKey(related_name='courses', verbose_name='SINIF', to='baseApp.Classroom', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(verbose_name='KOD', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='end',
            field=models.TimeField(verbose_name='BİTİŞ SAATİ', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='lisarLevel',
            field=models.CharField(verbose_name='LİSAR KADEMESİ', max_length=10, choices=[('1.', '1.'), ('2.', '2.')], null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(verbose_name='İSİM', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='start',
            field=models.TimeField(verbose_name='BAŞLANGIÇ SAATİ', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(to='baseApp.Teacher', verbose_name='ÖĞRETMEN', null=True),
        ),
        migrations.AlterField(
            model_name='createattendance',
            name='course',
            field=models.ForeignKey(to='baseApp.Course', verbose_name='DERS', null=True),
        ),
        migrations.AlterField(
            model_name='createattendance',
            name='date',
            field=models.DateField(verbose_name='TARİH', max_length=8, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='highschool',
            name='name',
            field=models.CharField(verbose_name='İSİM', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='highschool',
            name='schoolType',
            field=models.CharField(verbose_name='OKUL TİPİ', max_length=10, choices=[('Anadolu', 'Anadolu'), ('Fen', 'Fen'), ('İmam Hatip', 'İmam Hatip'), ('Anadolu İmam Hatip', 'Anadolu İmam Hatip')], null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(verbose_name='İSİM', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='schoolType',
            field=models.CharField(verbose_name='OKUL TİPİ', max_length=50, choices=[('Lisesi', 'Lise'), ('Üniversitesi', 'Üniversite')], null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='TEOGScore',
            field=models.FloatField(blank=True, verbose_name='TEOG SKORU', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='admissionCause',
            field=models.TextField(blank=True, verbose_name='BAŞVURU SEBEBİ', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='adress',
            field=models.CharField(blank=True, verbose_name='ADRES', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dateOfBirth',
            field=models.DateField(verbose_name='DOĞUM TARİHİ', max_length=8, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstName',
            field=models.CharField(verbose_name='İSİM', max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='highSchool',
            field=models.ForeignKey(blank=True, related_name='students', verbose_name='LİSE', to='baseApp.HighSchool', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(verbose_name='SOYİSİM', max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='lisarLevel',
            field=models.CharField(verbose_name='LİSAR KADEMESİ', max_length=10, default='1', choices=[('1', '1'), ('2', '2'), ('3', 'Mezun')]),
        ),
        migrations.AlterField(
            model_name='student',
            name='mailAddress',
            field=models.EmailField(blank=True, verbose_name='EMAIL ADRESİ', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parentMailAddress',
            field=models.EmailField(blank=True, verbose_name='VELİ EMAIL ADRESİ', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phoneNumber',
            field=models.CharField(blank=True, verbose_name='TELEFON', max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.", regex='^\\+?1?\\d{12}$')], null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='profilePhoto',
            field=models.ImageField(blank=True, verbose_name='FOTOĞRAF', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='reference',
            field=models.TextField(blank=True, verbose_name='REFERANSLAR', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='residence',
            field=models.CharField(blank=True, verbose_name='KALDIĞI YER', max_length=10, choices=[('Ev', 'Ev'), ('Yurt', 'Yurt')], null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='schoolLevel',
            field=models.CharField(verbose_name='SINIF', max_length=10, default='9', choices=[('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', 'Mezun')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='IBAN',
            field=models.CharField(blank=True, verbose_name='IBAN NO', max_length=26, validators=[django.core.validators.RegexValidator(message="IBAN must be entered in the format: 'TR999999999999999999999999'. 24 digits allowed.", regex='^\\w{2}\\d{24}$')], null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(blank=True, verbose_name='BÖLÜM', max_length=300, choices=[('bilgisayar mühendisliği', 'Bilgisayar Mühendisliği'), ('kimya', 'Kimya')], null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='firstName',
            field=models.CharField(verbose_name='İSİM', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='lastName',
            field=models.CharField(verbose_name='SOYİSİM', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mailAddress',
            field=models.EmailField(blank=True, verbose_name='EMAIL ADRESİ', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phoneNumber',
            field=models.CharField(blank=True, verbose_name='Telefon', max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.", regex='^\\+?1?\\d{12}$')], null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profilePhoto',
            field=models.ImageField(blank=True, verbose_name='FOTOĞRAF', upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(blank=True, related_name='teachers', verbose_name='OKUL', to='baseApp.School', null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='status',
            field=models.CharField(blank=True, verbose_name='STATÜ', max_length=30, choices=[('lisans', 'Lisans'), ('yüksek lisans', 'Yüksek Lisans'), ('doktora', 'Doktora')], null=True),
        ),
    ]
