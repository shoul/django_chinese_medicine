# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chinese_medicine', '0006_auto_20160331_2209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseasepattern',
            old_name='results',
            new_name='symptoms',
        ),
    ]
