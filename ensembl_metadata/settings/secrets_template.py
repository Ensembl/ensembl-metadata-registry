import ensembl_metadata.settings.env
# Make this unique
SECRET_KEY = '$@_oa*gtx=_xx$g+$u__^5@-#ig33rt$pcs%=zaiuq1*k4y&mn'

if ensembl_metadata.settings.env.TRAVIS_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
elif ensembl_metadata.settings.env.INTERNAL_PROD_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
elif ensembl_metadata.settings.env.PROD_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
elif ensembl_metadata.settings.env.DEV_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = '3306'
elif ensembl_metadata.settings.env.STAGING_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
else:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
