# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20170417_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='patient_name_first',
            field=models.CharField(max_length=255, verbose_name="patient's first name"),
        ),
        migrations.AlterField(
            model_name='application',
            name='patient_name_last',
            field=models.CharField(max_length=255, verbose_name="patient's second name"),
        ),
        migrations.AlterField(
            model_name='application',
            name='patient_name_middle',
            field=models.CharField(blank=True, max_length=255, verbose_name="patient's middle name"),
        ),
    ]
