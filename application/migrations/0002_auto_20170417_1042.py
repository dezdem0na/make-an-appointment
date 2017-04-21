# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-17 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.DateTimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=255)),
                ('name_middle', models.CharField(blank=True, max_length=255)),
                ('name_last', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name_plural': 'specialties'},
        ),
        migrations.AlterField(
            model_name='specialist',
            name='name_middle',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Specialty'),
        ),
        migrations.AddField(
            model_name='application',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Patient'),
        ),
        migrations.AddField(
            model_name='application',
            name='specialist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Specialist'),
        ),
    ]