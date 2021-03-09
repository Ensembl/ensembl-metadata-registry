import os

ENV = os.getenv('DJANGO_ENVIRONMENT', 'development')
DEV_ENV = ENV == 'development'
PROD_ENV = ENV == 'production'

METADATA_DB = os.getenv('METADATA_DB', 'ensembl_metadata')
TAXONOMY_DB = os.getenv('METADATA_DB', 'ncbi_taxonomy')

METADATA_DB_OLD = os.getenv('METADATA_DB_OLD')
