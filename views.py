# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views import generic as _gv
from django.core.urlresolvers import reverse_lazy

from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from .forms import ActivateSymptomForm
from .models import DiseasePattern, Symptom, Therapy, Etiologie



class DiseaseIndex(_gv.ListView):
    model = DiseasePattern
    ordering = ['name',]


class DiseaseDetail(_gv.DetailView):
    model = DiseasePattern


class DiseaseAdd(_gv.CreateView):
    model = DiseasePattern
    fields = ['name', 'slug', 'symptoms', 'manifestation', 'pathologie',
        'etiologie', 'therapy']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(DiseaseAdd, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Anlegen'))
        return form


class DiseaseEdit(_gv.UpdateView):
    model = DiseasePattern
    fields = ['name', 'slug', 'symptoms', 'manifestation', 'pathologie',
        'etiologie', 'therapy']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(DiseaseEdit, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', u'Ändern'))
        return form


class DiseaseRemove(_gv.DeleteView):
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


class SymptomIndex(_gv.ListView):
    model = Symptom
    ordering = ['localisation','indication']


class Main(_gv.ListView):
    model = Symptom
    template_name = 'django_chinese_medicine/main.html'

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


class SymptomDetail(_gv.DetailView):
    model = Symptom


class SymptomAdd(_gv.CreateView):
    model = Symptom
    fields = ['localisation', 'indication', 'slug', 'description']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(SymptomAdd, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Anlegen'))
        return form


class SymptomEdit(_gv.UpdateView):
    model = Symptom
    fields = ['localisation', 'indication', 'slug', 'description']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(SymptomEdit, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Bearbeiten'))
        return form


class SymptomRemove(_gv.DeleteView):
    model = Symptom
    fields = ['localisation', 'indication', 'slug', 'description']
    template_name = 'django_chinese_medicine/symptom_delete.html'
    success_url = reverse_lazy('symptom_index')

    def get_form(self, *args):
        form = super(SymptomRemove, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Schreddern'))
        return form


class TherapyIndex(_gv.ListView):
    model = Therapy
    ordering = ['name',]


class TherapyDetail(_gv.DetailView):
    model = Therapy


class TherapyCreate(_gv.CreateView):
    model = Therapy
    fields = ['name', 'intension', 'slug', 'description']


class TherapyEdit(_gv.UpdateView):
    model = Therapy
    fields = ['name', 'intension', 'slug', 'description']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(TherapyEdit, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Bearbeiten'))
        return form


class TherapyRemove(_gv.DeleteView):
    model = Therapy
    fields = ['name', 'intension', 'slug', 'description']
    template_name = 'django_chinese_medicine/therapy_delete.html'
    success_url = reverse_lazy('therapy_index')

    def get_form(self, *args):
        form = super(TherapyRemove, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Schreddern'))
        return form


class EtiologieIndex(_gv.ListView):
    model = Etiologie


class EtiologieDetail(_gv.DetailView):
    model = Etiologie


class EtiologieAdd(_gv.CreateView):
    model = Etiologie
    fields = ['name', 'slug', 'description']


class EtiologieEdit(_gv.UpdateView):
    model = Etiologie
    fields = ['name', 'slug', 'description']
    template_name = 'django_chinese_medicine/crispy_edit.html'

    def get_form(self, *args):
        form = super(EtiologieEdit, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Bearbeiten'))
        return form


class EtiologieRemove(_gv.DeleteView):
    model = Etiologie
    fields = ['name', 'slug', 'description']
    template_name = 'django_chinese_medicine/etiologie_delete.html'
    success_url = reverse_lazy('etiologie_index')

    def get_form(self, *args):
        form = super(EtiologieRemove, self).get_form(*args)
        form.helper = FormHelper()
        form.helper.add_input(Submit('submit', 'Schreddern'))
        return form

