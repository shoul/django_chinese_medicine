from django.conf.urls import url

from django_chinese_medicine import views

urlpatterns = [
    url(r'^krankheitsmuster/neu/$', views.DiseaseAdd.as_view(), name='disease_add'),
    url(r'^krankheitsmuster/(?P<slug>[-\w]+)/$', views.DiseaseDetailView.as_view(),
        name='disease_detail'),
    url(r'^krankheitsmuster/$', views.DiseaseListView.as_view(), name='disease_index'),
    url(r'^therapien/$', views.TherapyListView.as_view(), name='therapy_index'),
    url(r'^therapie/(?P<slug>[-\w]+)/$', views.TherapyDetail.as_view(),
    name='therapy_detail'),
    url(r'^therapy/add/$', views.TherapyCreate.as_view(), name='therapy_add'),
    url(r'^(?P<slug>[-\w]+)/$', views.SymptomDetail.as_view(),
        name='symptom_detail'),
    url(r'^$', views.SymptomIndex.as_view(), name='symptom_index'),
]
