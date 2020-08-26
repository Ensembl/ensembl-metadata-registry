# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='ensembl-metadata-registry',
    version='0.1',
    packages=find_packages(),
#    ['ensembl_metadata_registry',
#              'ensembl_metadata_registry.assembly',
#              'ensembl_metadata_registry.compara',
#              'ensembl_metadata_registry.datarelease',
#              ],
    package_dir={
        'ensembl_metadata_0_1': 'ensembl_metadata_reistry',
    },
    url='https://test-metadata-registry.ensembl.org',
    license='Apache',
    author='mchakiachvili',
    author_email='mchakiachvili@ebi.ac.uk',
    description='Alpha version for Ensembl metadata-registry'
)
