# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('baseApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=500)),
                ('schoolType', models.CharField(null=True, choices=[('Lisesi', 'Lise'), ('Üniversitesi', 'Üniversite')], blank=True, max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='IBAN',
            field=models.CharField(null=True, verbose_name='IBAN', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(null=True, verbose_name='Bölüm', blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='firstName',
            field=models.CharField(null=True, verbose_name='İsim', blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='lastName',
            field=models.CharField(null=True, verbose_name='Soyisim', blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='mailAddress',
            field=models.EmailField(null=True, verbose_name='Email Adresi', blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phoneNumber',
            field=models.CharField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. 12 digits allowed.", regex='^\\+?1?\\d{12}$')], verbose_name='Telefon', blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='school',
            field=models.ForeignKey(to='baseApp.School', blank=True, related_name='teachers', null=True, verbose_name='Okul'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='status',
            field=models.CharField(null=True, verbose_name='Statü', choices=[('lisans', 'Lisans'), ('yüksek lisans', 'Yüksek Lisans'), ('doktora', 'Doktora')], blank=True, max_length=30),
        ),
    ]
