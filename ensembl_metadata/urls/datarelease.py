from django.urls import path, re_path
from ensembl_metadata.views import datarelease


urlpatterns = [
    re_path(r'^(?P<version>[0-9]+)/(?P<site>[\w ]+)/$', datarelease.DataReleaseDetail.as_view()),
    re_path(r'^(?P<version>[0-9]+)/$', datarelease.DataReleaseList.as_view()),
    path('', datarelease.DataReleaseList.as_view()),
]
