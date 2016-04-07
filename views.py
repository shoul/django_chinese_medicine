from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.forms import modelformset_factory

from .models import DiseasePattern, Symptom, Therapy
from .forms import ActivateSymptomForm


class DiseaseListView(ListView):
    model = DiseasePattern
    ordering = ['name',]


class DiseaseDetailView(DetailView):
    model = DiseasePattern


class SymptomIndex(ListView):
    model = Symptom
    template_name = 'django_chinese_medicine/symptom_list.html'

    def get(self, request, *args, **kwargs):
        disease_list = DiseasePattern.objects.all().order_by('name')
        formset = ActivateSymptomForm()
        return render(request, self.template_name, {'formset': formset,
            'disease_list': disease_list})

    def post(self, request, *args, **kwargs):
        formset = ActivateSymptomForm(request.POST)

        if formset.is_valid():
            symptom_select_id = request.POST.getlist(u'symptom_select')
            disease_list = DiseasePattern.objects.all().order_by('name').filter(
                symptoms__id__in=symptom_select_id)

        return render(request, self.template_name, {'formset': formset,
            'disease_list': disease_list})


class SymptomDetail(DetailView):
    model = Symptom


class TherapyListView(ListView):
    model = Therapy
    ordering = ['name',]

class TherapyDetail(DetailView):
    model = Therapy
