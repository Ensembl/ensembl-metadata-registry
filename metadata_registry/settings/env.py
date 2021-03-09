import os

ENV = os.getenv('DJANGO_ENVIRONMENT', 'development')
DEV_ENV = ENV == 'development'
PROD_ENV = ENV == 'production'

REGISTRY_DB = os.getenv('REGISTRY_DB', 'metadata_registry')
METADATA_DB = os.getenv('METADATA_DB', 'ensembl_metadata')
TAXONOMY_DB = os.getenv('TAXONOMY_DB', 'ncbi_taxonomy')

METADATA_DB_OLD = os.getenv('METADATA_DB_OLD')
