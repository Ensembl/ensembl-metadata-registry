from .base import *

SECRET_KEY = 'test_secret_key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'metadata_registry',
        'TEST': {
            'DEPENDENCIES': ['ensembl_metadata', 'ncbi_taxonomy'],
        },
    },
    'ensembl_metadata': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ensembl_metadata',
        'TEST': {
            'DEPENDENCIES': ['ncbi_taxonomy'],
        },
    },
    'ncbi_taxonomy': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ncbi_taxonomy',
        'TEST': {
            'DEPENDENCIES': [],
        },
    }
}
