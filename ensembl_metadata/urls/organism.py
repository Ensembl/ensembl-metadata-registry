from django.urls import path, re_path
from ensembl_metadata.views import organism


urlpatterns = [
    re_path(r'^(?P<name>[\w.]+)/$', organism.OrganismDetail.as_view()),
    path('', organism.OrganismList.as_view()),
]
