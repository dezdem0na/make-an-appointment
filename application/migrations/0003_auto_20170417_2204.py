# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20170417_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='patient',
        ),
        migrations.AddField(
            model_name='application',
            name='patient_name_first',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='patient_name_last',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='patient_name_middle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='application',
            name='appointment',
            field=models.DateTimeField(unique=True, verbose_name='appointment'),
        ),
        migrations.AlterField(
            model_name='application',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Specialist', verbose_name='specialist'),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]