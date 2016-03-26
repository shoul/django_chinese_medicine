# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chinese_medicine', '0004_auto_20160324_1455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptom',
            name='active',
        ),
    ]
