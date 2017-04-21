# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 17:11
from __future__ import unicode_literals

import application.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20170418_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='appointment',
            field=models.DateTimeField(validators=[application.validators.validate_past], verbose_name='appointment'),
        ),
        migrations.AlterField(
            model_name='application',
            name='specialist',
            field=models.ForeignKey(error_messages={'unique_for_date': 'Sorry, this time slot is not available.'}, on_delete=django.db.models.deletion.CASCADE, to='application.Specialist', unique_for_date='appointment', verbose_name='specialist'),
        ),
    ]