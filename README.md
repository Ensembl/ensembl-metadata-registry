EMR - ensembl-metadata-registry
===============================


[![Documentation Status](https://readthedocs.org/projects/ensembl-metadata-registry/badge/?version=latest)](http://ensembl-metadata-registry.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/Ensembl/ensembl-metadata-registry.svg?branch=master)](https://travis-ci.org/Ensembl/ensembl-metadata-registry)

EMR - ensembl-metadata-registry

Provides RESTful data access to ensembl-metadata database over HTTP


# Requirements
- pyenv and pyenv-virtualenv or virtualenvwrapper
- Python 3.6+
- MySQL 5.6+


Installation
------------
Clone the project from git

```
git clone https://github.com/Ensembl/ensembl-metadata-registry.git
```

Create the Python environment

```
mkvirtualenv emrenv
workon emrenv

cd metadata_registry
pip install -r requirements.txt 

```

Provide the right credentials to connect to the ensembl-metata database in secrets.py (created from secrets_template.py)

```
cd metadata_registry/metadata_registry/metadata_registry/settings
cp secrets_template.py secrets.py

```

Provide the right credentials to connect to the django manager database (metadata_registry) in base.py
Note: All the django's management table while running the migration step will be created in metadata_registry
```
cd metadata_registry/metadata_registry/metadata_registry/settings

Look in the following section of base.py
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'metadata_registry',
            'USER': 'xxxx',
            'PASSWORD': 'xxxx',
            'HOST': 'localhost',
            'PORT': '3306',

```



Run the migrate step with --fake-initial (No need to run the migrations as the database is already there and it is not managed by Django)
```
./manage.py migrate --database meta metadata_registry --fake-initial
```

Start the development server
cd metadata_registry/metadata_registry/
```
 ./manage.py runserver 0:9000 --settings=ensembl_metadata.settings.local
```

Check in the browsesr
```
http://localhost:9000/
```


