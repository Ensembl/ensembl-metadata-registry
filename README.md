Ensembl Metadata Registry
===============================

[![Documentation Status](https://readthedocs.org/projects/ensembl-metadata-registry/badge/?version=latest)](http://ensembl-metadata-registry.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.org/Ensembl/ensembl-metadata-registry.svg?branch=master)](https://travis-ci.org/Ensembl/ensembl-metadata-registry)

Provides REST data access to ensembl-metadata database over HTTP

# Requirements
- Python 3.6+
- virtualenvwrapper
- MySQL 5.6+

Installation
------------
Clone the project from git
```
git clone https://github.com/Ensembl/ensembl-metadata-registry.git
```

Create the Python environment
```
mkvirtualenv emrenv -p /usr/bin/python3
workon emrenv

cd metadata_registry
pip install -r requirements.txt 
```

Provide the right credentials to connect to the ensembl-metadata database in secrets.py
```
cd metadata_registry/settings
cp secrets_template.py secrets.py
# Update ensembl_metadata/settings/secrets.py with a SECRET_KEY and database details.
```

Create an environment variable for the settings
```
export DJANGO_SETTINGS_MODULE=metadata_registry.settings.base
```

Run the migrate step, for a pre-existing database
```
./manage.py migrate --fake-initial
```

Start the development server
```
 ./manage.py runserver 0:9000
```

Check in the browser
```
http://localhost:9000/
```
