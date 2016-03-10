from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import DiseasePattern, Result


class DiseaseListView(ListView):
    model = DiseasePattern


class DiseaseDetailView(DetailView):
    model = DiseasePattern


class ResultIndex(ListView):
    model = Result


class ResultDetail(DetailView):
    model = Result
