# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 17:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temperature',
            old_name='temperature',
            new_name='tem_value',
        ),
    ]
