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

def get_int_from_string(string):
    ### TODO: Check int, write test
    import re
    p = re.compile('^.*(\d).*$')
    m = p.match(string)
    return int(m.groups()[0])

class SymptomIndex(ListView):
    model = Symptom
    template_name = 'django_chinese_medicine/symptom_list.html'
    ActivateSymptomFormSet = modelformset_factory(Symptom, 
        form=ActivateSymptomForm, extra=0)
    symptoms = Symptom.objects.all().order_by(*['spot', 'result'])

    def get(self, request, *args, **kwargs):
        data = { 'form-TOTAL_FORMS': len(self.symptoms),
            'form-MAX_FORMS': len(self.symptoms), 
            'form-INITIAL_FORMS': len(self.symptoms)}
        disease_list = DiseasePattern.objects.all().order_by('name')
        therapy_list = Therapy.objects.all().order_by('name')
        formset = self.ActivateSymptomFormSet(queryset=self.symptoms)
        return render(request, self.template_name, {'formset': formset,
            'disease_list': disease_list, 'therapy_list': therapy_list})

    def post(self, request, *args, **kwargs):
        # This method requires cashing the state of symptoms in get.
        formset = self.ActivateSymptomFormSet(request.POST)
        # get slug_list from fomset.data:
        slug_list = formset.data.getlist(u'slug', '')
        active_list = [get_int_from_string(k) for k, v in formset.data.items() 
            if v == u'on'] 
        active_slug_for_symptoms = [slug_list[i] for i in active_list]
        disease_list = DiseasePattern.objects.all().order_by('name').filter(
                symptoms__slug__in=active_slug_for_symptoms)
        therapy_list = Therapy.objects.all().order_by('name')
        return render(request, self.template_name, {'formset': formset,
            'disease_list': disease_list, 'therapy_list': therapy_list})


class SymptomDetail(DetailView):
    model = Symptom


class TherapyListView(ListView):
    model = Therapy
    ordering = ['name',]

class TherapyDetail(DetailView):
    model = Therapy
