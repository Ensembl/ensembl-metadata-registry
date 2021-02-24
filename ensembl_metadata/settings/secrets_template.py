import ensembl_metadata.settings.env
# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

if ensembl_metadata.settings.env.DEV_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = '3306'
elif ensembl_metadata.settings.env.PROD_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
else:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
