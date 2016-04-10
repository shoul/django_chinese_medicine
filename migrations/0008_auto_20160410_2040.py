# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chinese_medicine', '0007_auto_20160331_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='symptom',
            old_name='spot',
            new_name='localisation',
        ),
    ]
