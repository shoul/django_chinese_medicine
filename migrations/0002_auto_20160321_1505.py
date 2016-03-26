# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chinese_medicine', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Result',
            new_name='Symptom',
        ),
        migrations.AlterModelOptions(
            name='symptom',
            options={'verbose_name': 'Symptom', 'verbose_name_plural': 'Symptome'},
        ),
    ]
