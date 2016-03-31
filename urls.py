from django.conf.urls import url

from .views import (DiseaseListView, DiseaseDetailView, SymptomIndex,
    SymptomDetail, TherapyListView, TherapyDetail)

urlpatterns = [
    url(r'^krankheitsmuster/(?P<slug>[-\w]+)/$', DiseaseDetailView.as_view(),
        name='disease_detail'),
    url(r'^krankheitsmuster/$', DiseaseListView.as_view(), name='disease_index'),
    url(r'^therapien/$', TherapyListView.as_view(), name='therapy_index'),
    url(r'^therapie/(?P<slug>[-\w]+)/$', TherapyDetail.as_view(),
    name='therapy_detail'),
    url(r'^(?P<slug>[-\w]+)/$', SymptomDetail.as_view(),
        name='symptom_detail'),
    url(r'^$', SymptomIndex.as_view(), name='symptom_index'),
]
