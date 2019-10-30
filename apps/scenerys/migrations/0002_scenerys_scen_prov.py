# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-09 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0001_initial'),
        ('scenerys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenerys',
            name='scen_prov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='provinces.Provinces', verbose_name='景区省份'),
        ),
    ]