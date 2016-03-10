from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import DiseasePattern, Result, Therapy


class DiseaseListView(ListView):
    model = DiseasePattern


class DiseaseDetailView(DetailView):
    model = DiseasePattern


class ResultIndex(ListView):
    model = Result

    def get_context_data(self, **kwargs):
        context = super(ResultIndex, self).get_context_data(**kwargs)
        context['disease_list'] = DiseasePattern.objects.all()
        context['therapy_list'] = Therapy.objects.all()
        return context


class ResultDetail(DetailView):
    model = Result


class TherapyDetail(DetailView):
    model = Therapy
