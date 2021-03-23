import metadata_registry.settings.env
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'replace_me'

if metadata_registry.settings.env.DEV_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'localhost'
    DATABASE_PORT = '3306'
elif metadata_registry.settings.env.PROD_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
else:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
