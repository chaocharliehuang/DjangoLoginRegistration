# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-20 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_user_pw'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pw',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
