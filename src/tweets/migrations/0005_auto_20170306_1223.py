# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-06 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_auto_20170306_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=140, validators=[tweets.validators.validate_content]),
        ),
    ]
