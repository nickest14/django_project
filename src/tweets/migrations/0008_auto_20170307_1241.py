# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-07 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_auto_20170307_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
        migrations.DeleteModel(
            name='test',
        ),
    ]