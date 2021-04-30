from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('assembly/', include('ensembl_metadata.urls.assembly')),
    path('genome/', include('ensembl_metadata.urls.genome')),
    path('release/', include('ensembl_metadata.urls.release')),
    path('taxonomy/', include('ncbi_taxonomy.urls')),
    path(
        'schema/',
        SpectacularAPIView.as_view(),
        name='schema'),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            template_name='swagger-ui.html',
            url_name='schema',
        ),
        name='swagger-ui',
    ),
    path('', RedirectView.as_view(url='docs/')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
]
