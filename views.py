from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import DiseasePattern, Symptom, Therapy


class DiseaseListView(ListView):
    model = DiseasePattern
    ordering = ['name',]


class DiseaseDetailView(DetailView):
    model = DiseasePattern


class SymptomIndex(ListView):
    model = Symptom
    ordering = ['spot', 'result']

    def get_context_data(self, **kwargs):
        context = super(SymptomIndex, self).get_context_data(**kwargs)
        context['disease_list'] = DiseasePattern.objects.all().order_by('name')
        context['therapy_list'] = Therapy.objects.all().order_by('name')
        return context


class SymptomDetail(DetailView):
    model = Symptom


class TherapyListView(ListView):
    model = Therapy
    ordering = ['name',]

class TherapyDetail(DetailView):
    model = Therapy
