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
import metadata_registry.views.meta as views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^dashboard/ensembl', TemplateView.as_view(template_name="metadata_registry/meta_stats/dashboard_ens.html")),
    url(r'^(?P<division>[\w]+)/$', views.AggregatorView.as_view(), name='get_db_count'),
]
