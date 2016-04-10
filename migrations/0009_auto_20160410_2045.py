# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chinese_medicine', '0008_auto_20160410_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='symptom',
            old_name='result',
            new_name='indication',
        ),
    ]
