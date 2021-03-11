from .standard import *

INSTALLED_APPS += ['metadata_orm']

DATABASES.update({
    'metadata': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env.METADATA_DB_OLD,
        'USER': secrets.DATABASE_USER,
        'PASSWORD': secrets.DATABASE_PASSWORD,
        'HOST': secrets.DATABASE_HOST,
        'PORT': secrets.DATABASE_PORT,
    }})

DATABASE_ROUTERS += ['metadata_orm.router.MetadataOrmRouter']
