from django.conf.urls import url

from django_chinese_medicine import views

urlpatterns = [
    url(r'^krankheitsmuster/neu/$', views.DiseaseAdd.as_view(), name='disease_add'),
    url(r'^krankheitsmuster/$', views.DiseaseList.as_view(), name='disease_index'),
    url(r'^krankheitsmuster/(?P<slug>[-\w]+)/bearbeiten/$', views.DiseaseEdit.as_view(),
        name='disease_edit'),
    url(r'^krankheitsmuster/(?P<slug>[-\w]+)/$', views.DiseaseDetail.as_view(),
        name='disease_detail'),
    url(r'^therapien/$', views.TherapyList.as_view(), name='therapy_index'),
    url(r'^therapie/(?P<slug>[-\w]+)/$', views.TherapyDetail.as_view(),
    name='therapy_detail'),
    url(r'^therapy/add/$', views.TherapyCreate.as_view(), name='therapy_add'),
    url(r'^(?P<slug>[-\w]+)/$', views.SymptomDetail.as_view(),
        name='symptom_detail'),
    url(r'^$', views.SymptomIndex.as_view(), name='symptom_index'),
]
