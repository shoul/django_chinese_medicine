# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiseasePattern',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('manifestation', models.TextField(max_length=1024, blank=True)),
                ('pathologie', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'KrankheitsMuster',
                'verbose_name_plural': 'KrankheitsMuster',
            },
        ),
        migrations.CreateModel(
            name='Etiologie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=1024, blank=True)),
            ],
            options={
                'verbose_name': '\xc4tiologie',
                'verbose_name_plural': '\xc4tiologien',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('spot', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('result', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1024, blank=True)),
            ],
            options={
                'verbose_name': 'Befund',
                'verbose_name_plural': 'Befunde',
            },
        ),
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('intension', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(max_length=1024, blank=True)),
            ],
            options={
                'verbose_name': 'Therapie',
                'verbose_name_plural': 'Therapien',
            },
        ),
        migrations.AddField(
            model_name='diseasepattern',
            name='etiologie',
            field=models.ManyToManyField(to='django_chinese_medicine.Etiologie', blank=True),
        ),
        migrations.AddField(
            model_name='diseasepattern',
            name='results',
            field=models.ManyToManyField(to='django_chinese_medicine.Result', blank=True),
        ),
        migrations.AddField(
            model_name='diseasepattern',
            name='therapy',
            field=models.ManyToManyField(to='django_chinese_medicine.Therapy', blank=True),
        ),
    ]
