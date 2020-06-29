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


class EnsemblMetaDataRegistryRouter(object):
    """
    A router to control all database operations on models in the
    ensembl metadata registry.
    """
    META_DBS = ('metadata_registry')

    def db_for_read(self, model, **hints):
        """
        Attempts to read ncbi_taxonomy models go to ncbi_taxonomy.
        """
        if model._meta.app_label == 'ncbi_taxonomy':
            return 'ncbi_taxonomy'
        if model._meta.app_label in EnsemblMetaDataRegistryRouter.META_DBS:
            return 'meta'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write to dbs go to default.
        """
        if model._meta.app_label == 'ncbi_taxonomy':
            return 'ncbi_taxonomy'
        if model._meta.app_label in EnsemblMetaDataRegistryRouter.META_DBS:
            return 'meta'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """

        """
        if obj1._meta.app_label == 'ncbi_taxonomy' or \
           obj2._meta.app_label == 'ncbi_taxonomy':
            return True
        if obj1._meta.app_label in EnsemblMetaDataRegistryRouter.META_DBS or \
           obj2._meta.app_label in EnsemblMetaDataRegistryRouter.META_DBS:
            return True
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """

        """
        if app_label == 'ncbi_taxonomy':
            return db == 'ncbi_taxonomy'
        if app_label in EnsemblMetaDataRegistryRouter.META_DBS:
            return db == 'meta'
        return 'default'
