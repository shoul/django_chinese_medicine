# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-10 20:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0006_auto_20160310_0946'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Therapie',
            new_name='Therapy',
        ),
    ]