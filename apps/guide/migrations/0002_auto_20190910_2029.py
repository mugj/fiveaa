# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-09-10 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide',
            name='title',
            field=models.CharField(max_length=50, verbose_name='标题'),
        ),
    ]