# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chinese_medicine', '0002_auto_20160321_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
