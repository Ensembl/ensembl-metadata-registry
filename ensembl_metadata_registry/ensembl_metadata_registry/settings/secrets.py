import ensembl_metadata_registry.settings.env
# Make this unique, and don't share it with anybody.
SECRET_KEY = '$@_oa*gtx=_xx$g+$u__^5@-#ig33rt$pcs%=zaiuq1*k4y&mn'

if ensembl_metadata_registry.settings.env.TEST_ENV:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
else:
    DATABASE_USER = 'readuser'
    DATABASE_PASSWORD = 'password'
    DATABASE_HOST = 'host'
    DATABASE_PORT = 'port'
