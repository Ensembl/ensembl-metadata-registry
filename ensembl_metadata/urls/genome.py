from django.urls import path, re_path
from ensembl_metadata.views import genome


urlpatterns = [
    re_path(r'^(?P<genome_uuid>[\w-]+)/$', genome.GenomeDetail.as_view()),
    path('', genome.GenomeList.as_view()),
]
