# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views import generic as gnrc
from django.core.urlresolvers import reverse_lazy

from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from .models import DiseasePattern, Symptom, Therapy
from .forms import ActivateSymptomForm

from .models import DiseasePattern, Symptom, Therapy, Etiologie


class DiseaseList(gnrc.ListView):
    model = DiseasePattern
    ordering = ['name',]


class DiseaseDetail(gnrc.DetailView):
    model = DiseasePattern


class DiseaseAdd(gnrc.CreateView):
    model = DiseasePattern
    fields = ['name', 'slug', 'symptoms', 'manifestation', 'pathologie',
        'etiologie', 'therapy']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(DiseaseAdd, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Anlegen'))
        return form


class DiseaseEdit(gnrc.UpdateView):
    model = DiseasePattern
    fields = ['name', 'slug', 'symptoms', 'manifestation', 'pathologie',
        'etiologie', 'therapy']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(DiseaseEdit, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', u'Ändern'))
        return form


class DiseaseRemove(gnrc.DeleteView):
    model = DiseasePattern
    fields = ['name', 'slug', 'symptoms', 'manifestation', 'pathologie',
        'etiologie', 'therapy']
    template_name = 'django_chinese_medicine/disease_pattern_delete.html'
    success_url = reverse_lazy('disease_index')

    def get_form(self, *args):
        form = super(DiseaseRemove, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', u'Schreddern'))
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


class SymptomAdd(gnrc.CreateView):
    model = Symptom
    fields = ['spot', 'result', 'slug', 'description']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(SymptomAdd, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Anlegen'))
        return form


class SymptomEdit(gnrc.UpdateView):
    model = Symptom
    fields = ['spot', 'result', 'slug', 'description']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(SymptomEdit, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Bearbeiten'))
        return form


class SymptomRemove(gnrc.DeleteView):
    model = Symptom
    fields = ['spot', 'result', 'slug', 'description']
    template_name = 'django_chinese_medicine/symptom_delete.html'
    success_url = reverse_lazy('symptom_index')

    def get_form(self, *args):
        form = super(SymptomRemove, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Schreddern'))
        return form


class TherapyList(gnrc.ListView):
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

