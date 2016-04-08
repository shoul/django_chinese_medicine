# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views import generic as gnrc

from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from .models import DiseasePattern, Symptom, Therapy
from .forms import ActivateSymptomForm

from .models import DiseasePattern, Symptom, Therapy, Etiologie


class DiseaseListView(gnrc.ListView):
    model = DiseasePattern
    ordering = ['name',]


class DiseaseDetailView(gnrc.DetailView):
    model = DiseasePattern


class DiseaseAdd(gnrc.CreateView):
    model = DiseasePattern
    fields = ['name', 'slug', 'symptoms', 'manifestation', 'pathologie',
        'etiologie', 'therapy']

    def get_form(self, *args):
        form = super(DiseaseAdd, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Anlegen'))
        return form


class SymptomIndex(gnrc.ListView):
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


class SymptomDetail(gnrc.DetailView):
    model = Symptom


class SymptomCreate(gnrc.CreateView):
    model = Symptom
    fields = ['spot', 'slug', 'result', 'description']


class TherapyListView(gnrc.ListView):
    model = Therapy
    ordering = ['name',]


class TherapyDetail(gnrc.DetailView):
    model = Therapy


class TherapyCreate(gnrc.CreateView):
    model = Therapy
    fields = ['name', 'intension', 'slug', 'description']


class EtiologieList(gnrc.ListView):
    model = Etiologie


class EtiologieDetail(gnrc.DetailView):
    model = Etiologie


class EtiologieCreate(gnrc.CreateView):
    model = Etiologie
    fields = ['name', 'slug', 'description']

