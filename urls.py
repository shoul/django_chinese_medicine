from django.conf.urls import url

from django_chinese_medicine import views

urlpatterns = [
    url(r'^krankheitsmuster/neu/$', views.DiseaseAdd.as_view(), name='disease_add'),
    url(r'^krankheitsmuster/$', views.DiseaseList.as_view(), name='disease_index'),
    url(r'^krankheitsmuster/(?P<slug>[-\w]+)/schreddern/$', views.DiseaseRemove.as_view(),
        name='disease_remove'),
    url(r'^krankheitsmuster/(?P<slug>[-\w]+)/bearbeiten/$', views.DiseaseEdit.as_view(),
        name='disease_edit'),
    url(r'^krankheitsmuster/(?P<slug>[-\w]+)/$', views.DiseaseDetail.as_view(),
        name='disease_detail'),
    url(r'^therapien/$', views.TherapyList.as_view(), name='therapy_index'),
    url(r'^therapie/(?P<slug>[-\w]+)/$', views.TherapyDetail.as_view(),
    name='therapy_detail'),
    url(r'^therapy/add/$', views.TherapyCreate.as_view(), name='therapy_add'),
    url(r'^symptom/neu/$', views.SymptomAdd.as_view(), name='symptom_add'),
    url(r'^symptom/(?P<slug>[-\w]+)/schreddern/$', views.SymptomRemove.as_view(),
        name='symptom_remove'),
    url(r'^symptom/(?P<slug>[-\w]+)/bearbeiten/$', views.SymptomEdit.as_view(),
        name='symptom_edit'),
    url(r'^symptom/(?P<slug>[-\w]+)/$', views.SymptomDetail.as_view(),
        name='symptom_detail'),
    url(r'^symptome/$', views.SymptomIndex.as_view(), name='symptom_index'),
    url(r'^$', views.Main.as_view(), name='main'),
]
