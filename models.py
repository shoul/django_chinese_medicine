# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models
from django.utils.text import slugify


class Symptom(models.Model):
    localisation = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    indication = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=1024)

    class Meta:
        verbose_name = u'Symptom'
        verbose_name_plural = u'Symptome'

    def __unicode__(self):
        return '%s: %s' % (self.localisation, self.indication)

    def get_absolute_url(self):
        return reverse('symptom_detail', kwargs={'slug': self.slug})


class Etiologie(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, max_length=1024)

    class Meta:
        verbose_name = u'Ätiologie'
        verbose_name_plural = u'Ätiologien'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('etiologie_detail', kwargs={'slug': self.slug})


class DiseasePattern(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    symptoms = models.ManyToManyField(Symptom, blank=True)
    manifestation = models.TextField(blank=True, max_length=1024)
    pathologie = models.TextField(max_length=255, blank=True)
    etiologie = models.ManyToManyField(Etiologie, blank=True)
    therapy = models.ManyToManyField('Therapy', blank=True)

    class Meta:
        verbose_name = u'KrankheitsMuster'
        verbose_name_plural = u'KrankheitsMuster'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('disease_detail', kwargs={'slug': self.slug})


class Therapy(models.Model):
    name = models.CharField(max_length=255)
    intension = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, max_length=1024)

    class Meta:
        verbose_name = u'Therapie'
        verbose_name_plural = u'Therapien'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('therapy_detail', kwargs={'slug': self.slug})
