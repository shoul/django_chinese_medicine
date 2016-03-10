from django.conf.urls import url

from .views import (DiseaseListView, DiseaseDetailView, ResultIndex,
    ResultDetail)

urlpatterns = [
    url(r'^krankheitsmuster/(?P<slug>[-\w]+)/$', DiseaseDetailView.as_view(),
        name='disease_detail'),
    url(r'^krankheitsmuster/$', DiseaseListView.as_view(), name='disease_index'),
    url(r'^(?P<slug>[-\w]+)/$', ResultDetail.as_view(),
        name='result_detail'),
    url(r'^$', ResultIndex.as_view(), name='result_index'),
]
