# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chinese_medicine', '0005_remove_symptom_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasepattern',
            name='pathologie',
            field=models.TextField(max_length=255, blank=True),
        ),
    ]
