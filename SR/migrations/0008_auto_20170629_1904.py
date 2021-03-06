# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 00:04
from __future__ import unicode_literals

import SR.utilidades
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR', '0007_auto_20170628_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='speech_recognition',
            name='text_cleaned',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='speech_recognition',
            name='audioFile',
            field=models.FileField(upload_to='audios/%Y/%m/%d/', validators=[SR.utilidades.audioFile_validator_manual]),
        ),
    ]
