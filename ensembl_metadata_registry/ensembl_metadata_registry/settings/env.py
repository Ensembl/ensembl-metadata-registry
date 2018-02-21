import os


ENV = os.getenv('DJANGO_ENVIRONMENT', 'development')
DEV_ENV = ENV == 'development'
TRAVIS_ENV = ENV == 'travis'
PROD_ENV = ENV == 'production'
INTERNAL_PROD_ENV = ENV == 'internal_production'
STAGING_ENV = ENV == 'staging'
