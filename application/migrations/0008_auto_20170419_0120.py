# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20170419_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Specialist', verbose_name='specialist'),
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set([('appointment', 'specialist')]),
        ),
    ]