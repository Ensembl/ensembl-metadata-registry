from django.urls import path, re_path
from ensembl_metadata.views import assembly


urlpatterns = [
    re_path(r'^(?P<accession>[\w.]+)/sequence/$', assembly.AssemblySequenceList.as_view()),
    re_path(r'^(?P<accession>[\w.]+)/$', assembly.AssemblyDetail.as_view()),
    path('', assembly.AssemblyList.as_view()),
]
