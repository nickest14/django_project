# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-06 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0016_auto_20170531_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.ImageField(height_field='height_field', null=True, upload_to=tweets.models.upload_location, width_field='width_field'),
        ),
    ]
