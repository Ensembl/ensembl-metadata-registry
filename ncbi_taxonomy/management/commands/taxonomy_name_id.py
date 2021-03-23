from django.core.management.base import BaseCommand
from django.db import transaction, connections

# The name table in the taxonomy db does not have a primary key defined;
# when we initially migrate, we use 'fake-initial' since the db is
# pre-existing. But that then means there is a ghost 'id' pk automatically
# added, which doesn't correspond to a database column.
# We could add a migration, but that breaks when we want to generate a
# test database; so we here define a command to add a primary key,
# designed to be run once, immediately after the fake-initial migration.


class Command(BaseCommand):
    help = 'Add a primary key to the taxonomy name table'

    def handle(self, *args, **options):
        auto_inc_sql = \
            'ALTER TABLE ncbi_taxa_name ADD COLUMN name_id INT AUTO_INCREMENT PRIMARY KEY FIRST'
        cursor = connections['ncbi_taxonomy'].cursor()
        cursor.execute(auto_inc_sql)
