from django.urls import path, re_path
from ensembl_metadata.views import release


urlpatterns = [
    re_path(r'^(?P<version>[0-9]+)/(?P<site>[\w ]+)/$', release.ReleaseDetail.as_view()),
    re_path(r'^(?P<version>[0-9]+)/$', release.ReleaseList.as_view()),
    path('', release.ReleaseList.as_view()),
]
