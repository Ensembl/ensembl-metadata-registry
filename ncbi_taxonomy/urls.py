from django.urls import path, re_path
from ncbi_taxonomy import views


urlpatterns = [
    re_path(r'^(?P<taxon_id>[0-9]+)/$', views.TaxonomyNodeDetail.as_view()),
    path('', views.TaxonomyNodeList.as_view()),
    path('names/', views.TaxonomyNameList.as_view())
]
