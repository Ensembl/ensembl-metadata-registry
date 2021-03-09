"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from .base import *  # @UnusedWildImport

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
