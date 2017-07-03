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
from ncbi_taxonomy import views

urlpatterns = [
    url(r'^taxonomy_node/$', views.NcbiTaxaNodeList.as_view(), name='ncbi_taxonomy_node_list'),
    url(r'^taxonomy_node/(?P<pk>[0-9]+)/$', views.NcbiTaxaNodeDetail.as_view(), name='ncbi_taxonomy_node_detail'),

    url(r'^taxonomy_name/$', views.NcbiTaxaNameList.as_view(), name='ncbi_taxonomy_name_detail'),
    url(r'^taxonomy_name/(?P<pk>[0-9]+)/$', views.NcbiTaxaNameDetail.as_view(), name='ncbi_taxonomy_name_detail'),
]
