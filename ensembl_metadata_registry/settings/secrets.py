import ensembl_metadata_registry.settings.env
# Make this unique, and don't share it with anybody.
SECRET_KEY = '$@_oa*gtx=_xx$g+$u__^5@-#ig33rt$pcs%=zaiuq1*k4y&mn'

if ensembl_metadata_registry.settings.env.TRAVIS_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
elif ensembl_metadata_registry.settings.env.INTERNAL_PROD_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
elif ensembl_metadata_registry.settings.env.PROD_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
elif ensembl_metadata_registry.settings.env.DEV_ENV:
    DATABASE_USER = 'ensembl'
    DATABASE_PASSWORD = 'ensembl'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = '3306'
elif ensembl_metadata_registry.settings.env.STAGING_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
else:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
