# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


class Result(models.Model):
    spot = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    result = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=1024)

    class Meta:
        verbose_name = u'Befund'
        verbose_name_plural = u'Befunde'

    def __unicode__(self):
        return '%s: %s' % (self.spot, self.result)


class Etiologie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, max_length=1024)

    class Meta:
        verbose_name = u'Ätiologie'
        verbose_name_plural = u'Ätiologien'

    def __unicode__(self):
        return self.name


class DiseasePattern(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    results = models.ManyToManyField(Result, blank=True)
    manifestation = models.TextField(blank=True, max_length=1024)
    tongue = models.TextField(blank=True, max_length=1024)
    puls = models.CharField(max_length=255)
    pathologie = models.CharField(max_length=255)
    etiologie = models.ManyToManyField(Etiologie, blank=True)

    class Meta:
        verbose_name = u'TherapieMuster'
        verbose_name_plural = u'TherapieMuster'

    def __unicode__(self):
        return self.name


class Therapie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    disease = models.ForeignKey(DiseasePattern, on_delete=models.CASCADE,
        blank=True)
    description = models.TextField(blank=True, max_length=1024)

    class Meta:
        verbose_name = u'Therapie'
        verbose_name_plural = u'Therapien'

    def __unicode__(self):
        return self.name
