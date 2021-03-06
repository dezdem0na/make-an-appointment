# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20170417_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='patient_name_first',
            field=models.CharField(max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='application',
            name='patient_name_last',
            field=models.CharField(max_length=255, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='application',
            name='patient_name_middle',
            field=models.CharField(blank=True, max_length=255, verbose_name='Отчество'),
        ),
    ]
