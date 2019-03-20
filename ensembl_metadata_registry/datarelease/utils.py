'''
Copyright [1999-2015] Wellcome Trust Sanger Institute and the EMBL-European Bioinformatics Institute
Copyright [2016-2019] EMBL-European Bioinformatics Institute

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
from datarelease.models import DataRelease


class DataReleaseUtils(object):

    @classmethod
    def get_latest_ensembl_version(cls):
        datarelease = None
        try:
            datarelease = DataRelease.objects.filter(is_current=1)[0]
        except:
            return None

        if datarelease is not None:
            return datarelease.ensembl_version
        return None

    @classmethod
    def get_latest_ensemblgenomes_version(cls):
        datarelease = None
        try:
            datarelease = DataRelease.objects.filter(is_current=1)[0]
        except:
            return None

        if datarelease is not None:
            return datarelease.ensembl_genomes_version
        return None
