from .base import *
from metadata_registry.settings import env
from metadata_registry.settings import secrets

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.SECRET_KEY

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.REGISTRY_DB,
        'USER': secrets.DATABASE_USER,
        'PASSWORD': secrets.DATABASE_PASSWORD,
        'HOST': secrets.DATABASE_HOST,
        'PORT': secrets.DATABASE_PORT,
        'TEST': {
            'DEPENDENCIES': ['ensembl_metadata', 'ncbi_taxonomy'],
        },
    },
    'ensembl_metadata': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.METADATA_DB,
        'USER': secrets.DATABASE_USER,
        'PASSWORD': secrets.DATABASE_PASSWORD,
        'HOST': secrets.DATABASE_HOST,
        'PORT': secrets.DATABASE_PORT,
        'TEST': {
            'DEPENDENCIES': ['ncbi_taxonomy'],
        },
    },
    'ncbi_taxonomy': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.TAXONOMY_DB,
        'USER': secrets.DATABASE_USER,
        'PASSWORD': secrets.DATABASE_PASSWORD,
        'HOST': secrets.DATABASE_HOST,
        'PORT': secrets.DATABASE_PORT,
        'TEST': {
            'DEPENDENCIES': [],
        },
    }
}
