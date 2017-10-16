'''
Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2017] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


from django.conf.urls import url
from organism import views
from organism.views import OrganismDatatableView

urlpatterns = [

    url(r'^$', views.OrganismList.as_view(), name='organism_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.OrganismDetail.as_view(), name='organism_detail'),

    url(r'^alias/$', views.OrganismAliasList.as_view(), name='organism_alias_list'),
    url(r'^alias/(?P<pk>[0-9]+)/$', views.OrganismAliasDetail.as_view(), name='organism_alias_detail'),

    url(r'^publication/$', views.OrganismPublicationList.as_view(), name='organism_publication_list'),
    url(r'^publication/(?P<pk>[0-9]+)/$', views.OrganismPublicationDetail.as_view(),
        name='organism_publication_detail'),
    # url(r'^nopagination', views.OrganismInfoView.as_view(), name="organism_info_nopagination_table"),
    url(r'^datatablefetch_serverside', OrganismDatatableView.as_view(),
        name="datatablefetch_serverside_organism"),

]
