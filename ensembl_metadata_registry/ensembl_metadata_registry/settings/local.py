from .base import *  # @UnusedWildImport

DEBUG = True

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1', 'localhost', 'prem-ml.local')
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
       'debug_toolbar',
    )

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ensembl_metadata_registry',
        'USER': 'xxxx',
        'PASSWORD': 'xxxx',
        'HOST': 'xxxx',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },
    'meta': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ensembl_metadata',
        'USER': 'xxxx',
        'PASSWORD': 'xxxx',
        'HOST': 'xxxx',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },
    'ncbi_taxonomy': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ncbi_taxonomy',
        'USER': 'xxxx',
        'PASSWORD': 'xxxx',
        'HOST': 'xxxx',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
