# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, find_namespace_packages

setup(
    name='ensembl_metadata_0_1',
    version='0.1',
    packages=find_namespace_packages(),
    package_dir={
        'ensembl_metadata_0_1': 'ensembl_metadata_registry'
    },
    url='https://test-metadata-registry.ensembl.org',
    license='Apache',
    author='mchakiachvili',
    author_email='mchakiachvili@ebi.ac.uk',
    description='Alpha version for Ensembl metadata-registry'
)
