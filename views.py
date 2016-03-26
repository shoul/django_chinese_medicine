from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import DiseasePattern, Symptom, Therapy


class DiseaseListView(ListView):
    model = DiseasePattern


class DiseaseDetailView(DetailView):
    model = DiseasePattern


class SymptomIndex(ListView):
    model = Symptom

    def get_context_data(self, **kwargs):
        context = super(SymptomIndex, self).get_context_data(**kwargs)
        context['disease_list'] = DiseasePattern.objects.all()
        context['therapy_list'] = Therapy.objects.all()
        return context


class SymptomDetail(DetailView):
    model = Symptom


class TherapyDetail(DetailView):
    model = Therapy
