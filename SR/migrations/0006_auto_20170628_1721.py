# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 22:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR', '0005_auto_20170617_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speech_recognition',
            name='audioFile',
            field=models.FileField(upload_to='audios/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.mp3', '.wav', '.flv', '.ogg'], code='invalid_extension', message="La extension '%(extension)s' No está permitida. Las extensiones permitidas son: '%(allowed_extensions)s'.")]),
        ),
    ]
