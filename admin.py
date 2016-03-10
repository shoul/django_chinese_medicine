from django.contrib import admin

from .models import Etiologie, DiseasePattern, Therapie, Result


@admin.register(Etiologie, DiseasePattern, Therapie)
class MyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('spot', 'result')}
