"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from django.conf.urls import url
from django.views.generic.base import TemplateView

import metadata_registry.views.genomeinfo as views
from metadata_registry.utils.datarelease import DataReleaseUtils

urlpatterns = [
    url(r'^$', views.GenomeList.as_view(), name='genome_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.GenomeDetail.as_view(), name='genome_detail'),

    url(r'^alignment/$', views.GenomeAlignmentList.as_view(), name='genome_alignment_list'),
    url(r'^alignment/(?P<pk>[0-9]+)/$', views.GenomeAlignmentDetail.as_view(), name='genome_alignment_detail'),

    url(r'^annotation/$', views.GenomeAnnotationList.as_view(), name='genome_annotation_list'),
    url(r'^annotation/(?P<pk>[0-9]+)/$', views.GenomeAnnotationDetail.as_view(), name='genome_annotation_detail'),

    url(r'^compara_analysis/$', views.GenomeComparaAnalysisList.as_view(), name='genome_compara_analysis_list'),
    url(r'^compara_analysis/(?P<pk>[0-9]+)/$',
        views.GenomeComparaAnalysisDetail.as_view(), name='genome_compara_analysis_detail'),

    url(r'^database/$', views.GenomeDatabaseList.as_view(), name='genome_database_list'),
    url(r'^database/(?P<pk>[0-9]+)/$', views.GenomeDatabaseDetail.as_view(), name='genome_database_detail'),

    url(r'^event/$', views.GenomeEventList.as_view(), name='genome_event_list'),
    url(r'^event/(?P<pk>[0-9]+)/$', views.GenomeEventDetail.as_view(), name='genome_event_detail'),

    url(r'^feature/$', views.GenomeFeatureList.as_view(), name='genome_feature_list'),
    url(r'^feature/(?P<pk>[0-9]+)/$', views.GenomeFeatureDetail.as_view(), name='genome_feature_detail'),

    url(r'^variationcount/$', views.GenomeVariationList.as_view(), name='genome_variation_list'),
    url(r'^variationcount/(?P<pk>[0-9]+)/$', views.GenomeVariationDetail.as_view(), name='genome_variation_detail'),

    # for genomeinfo datatable
    url(r'^info/division/(?P<division>[\w]+)/release/' + str(DataReleaseUtils.get_latest_ensembl_version()),
        TemplateView.as_view(template_name="metadata_registry/genomeinfo/datatable_ens.html"), name="genomeinfo_ens_table"),
    url(r'^info/division/(?P<division>[\w]+)/release/' + str(DataReleaseUtils.get_latest_ensemblgenomes_version()),
        TemplateView.as_view(template_name="metadata_registry/genomeinfo/datatable_ens.html"), name="genomeinfo_eg_table"),
    url(r'^nopagination', views.GenomeInfoView.as_view(), name="genomeinfo_nopagination_ens_table"),

]
