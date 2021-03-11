from .base import *
from metadata_registry.settings import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'test_secret_key'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env.REGISTRY_DB,
        'TEST': {
            'DEPENDENCIES': ['ensembl_metadata', 'ncbi_taxonomy'],
        },
    },
    'ensembl_metadata': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env.METADATA_DB,
        'TEST': {
            'DEPENDENCIES': ['ncbi_taxonomy'],
        },
    },
    'ncbi_taxonomy': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env.TAXONOMY_DB,
        'TEST': {
            'DEPENDENCIES': [],
        },
    }
}
