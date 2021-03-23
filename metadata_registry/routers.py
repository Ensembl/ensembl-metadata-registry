
class MetaDataRegistryRouter(object):
    """
    A router to direct operations in the metadata registry to either
    the metadata or taxonomy databases.
    """
    app_labels = {'ensembl_metadata', 'ncbi_taxonomy'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'ncbi_taxonomy':
            return 'ncbi_taxonomy'
        if model._meta.app_label == 'ensembl_metadata':
            return 'ensembl_metadata'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'ncbi_taxonomy':
            return 'ncbi_taxonomy'
        if model._meta.app_label == 'ensembl_metadata':
            return 'ensembl_metadata'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Within db relations are fine, also allow links between
        metadata and taxonomy databases.
        """
        if obj1._meta.app_label in self.app_labels and \
           obj2._meta.app_label in self.app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Migrations for a specific app are restricted to the appropriate database.
        """
        if app_label == 'ncbi_taxonomy':
            return db == 'ncbi_taxonomy'
        if app_label == 'ensembl_metadata':
            return db == 'ensembl_metadata'
        return None
