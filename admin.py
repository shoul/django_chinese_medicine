from django.contrib import admin

from .models import Etiologie, DiseasePattern, Therapy, Symptom


@admin.register(Etiologie, DiseasePattern)
class MyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name',]


@admin.register(Symptom)
class SymptomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('localisation', 'indication')}
    ordering = ['localisation', 'indication']

@admin.register(Therapy)
class Therapy(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'intension')}
    ordering = ['name',]
