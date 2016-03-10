from django.conf.urls import url

from .views import (DiseaseListView, DiseaseDetailView, ResultIndex,
    ResultDetail)

urlpatterns = [
    url(r'^befunde/$', ResultIndex.as_view(), name='result_index'),
    url(r'^befund/(?P<slug>[-\w]+)/$', ResultDetail.as_view(),
        name='result_detail'),
    url(r'^(?P<slug>[-\w]+)/$', DiseaseDetailView.as_view(),
        name='disease_detail'),
    url(r'^$', DiseaseListView.as_view(), name='diesase_index'),
]
