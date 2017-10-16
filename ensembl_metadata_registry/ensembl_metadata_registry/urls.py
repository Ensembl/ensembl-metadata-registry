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

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from ensembl_metadata_registry import routers
from ensembl_metadata_registry.views import datatable_view, datatable_fetch
from django.conf import settings


"""
ensembl_metadata_registry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

schema_view = get_swagger_view(title='Ensembl Metadata Registry REST API Endpoints')

router = routers.EnsemblMetaDataRegistryRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', schema_view),
    url(r'^$', schema_view),

    url(r'^assembly/', include('assembly.urls')),
    url(r'^compara_analysis/', include('compara.urls')),
    url(r'^datarelease/', include('datarelease.urls')),
    url(r'^division/', include('division.urls')),
    url(r'^genome/', include('genomeinfo.urls')),
    url(r'^ncbi_taxonomy/', include('ncbi_taxonomy.urls')),
    url(r'^organism/', include('organism.urls')),
    url(r'^meta_stats/', include('meta_stats.urls')),
    # for datatables
    url(r'^datatable/(?P<table_name>[\w]+)/', datatable_view, name="datatable_view"),
    url(r'^datatablefetch_clientside/(?P<table_name>[\w]+)/', datatable_fetch, name="datatablefetch_clientside"),
    # url(r'^datatablefetch_serverside/organism', OrganismDatatableView.as_view(),
    #    name="datatablefetch_serverside_organism"),




]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
