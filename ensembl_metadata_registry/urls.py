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

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from rest_framework_swagger.views import get_swagger_view

from metadata_registry.views.assembly import AssemblyDatatableView
from metadata_registry.views.base import datatable_view, datatable_fetch
from metadata_registry.views.datarelease import DataReleaseDatatableView
from metadata_registry.views.division import DivisionDatatableView
from metadata_registry.views.genomeinfo import GenomeDatatableView
from metadata_registry.views.organism import OrganismDatatableView

emr_apis = [
    url(r'^assembly/', include('metadata_registry.urls.assembly')),
    url(r'^compara_analysis/', include('metadata_registry.urls.compara')),
    url(r'^datarelease/', include('metadata_registry.urls.datarelease')),
    url(r'^division/', include('metadata_registry.urls.division')),
    url(r'^genome/', include('metadata_registry.urls.genomeinfo')),
    url(r'^ncbi_taxonomy/', include('ncbi_taxonomy.urls')),
    url(r'^organism/', include('metadata_registry.urls.organism')),
    url(r'^meta_stats/', include('metadata_registry.urls.meta')),
]

schema_view = get_swagger_view(title='Ensembl Metadata Registry REST API Endpoints', patterns=emr_apis)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', schema_view, name='doc_view'),
    url(r'^$', schema_view, name='home_view'),

]

internal_apis = [
    # for datatables
    url(r'^datatable/(?P<table_name>[\w]+)/', datatable_view, name="datatable_view"),

    # FIXME this url doens't work but doesn't seem to be used anywhere, anyway.
    # url(r'^datatable_clientside/(?P<table_name>[\w]+)/', datatable_fetch, name="datatablefetch_clientside"),

    url(r'^datatable_serverside/assembly', AssemblyDatatableView.as_view(),
        name="datatablefetch_serverside_assembly"),

    url(r'^datatable_serverside/organism', OrganismDatatableView.as_view(),
        name="datatablefetch_serverside_organism"),

    url(r'^datatable_serverside/genome', GenomeDatatableView.as_view(),
        name="datatablefetch_serverside_genome"),

    url(r'^datatable_serverside/division', DivisionDatatableView.as_view(),
        name="datatablefetch_serverside_division"),

    url(r'^datatable_serverside/datarelease', DataReleaseDatatableView.as_view(),
        name="datatablefetch_serverside_datarelease"),
    url(r'^privacy_notice_emr', TemplateView.as_view(template_name='metadata_registry/privacy_notice_emr.html'),
        name="privacy_note_emr"),
    # for datatables
    url(r'^datatable/(?P<table_name>[\w]+)/', datatable_view, name="datatable_view"),

    # FIXME this url doens't work but doesn't seem to be used anywhere, anyway.
    # url(r'^datatable_clientside/(?P<table_name>[\w]+)/', datatable_fetch, name="datatablefetch_clientside"),
]

urlpatterns = urlpatterns + emr_apis + internal_apis

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      url(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
