#!/usr/bin/env python
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
'''
This script is intended to allow import migration from pre-2020 Ensembl metadata schema onto the new scheme

Authors: Thomas Maurel / Marc Chakiachvili
'''
from django.conf import settings

from metadata_orm.models import Assembly as AssemblyCurrent, AssemblySequence as AssemblySequenceCurrent, \
    ComparaAnalysis as ComparaAnalysisCurrent, \
    ComparaAnalysisEvent as ComparaAnalysisEventCurrent, \
    DataRelease as DataReleaseCurrent, Division as DivisionCurrent, \
    Genome as GenomeCurrent, GenomeAlignment as GenomeAlignmentCurrent, GenomeAnnotation as GenomeAnnotationCurrent, \
    GenomeComparaAnalysis as GenomeComparaAnalysisCurrent, GenomeDatabase as GenomeDatabaseCurrent, \
    GenomeEvent as GenomeEventCurrent, GenomeFeature as GenomeFeatureCurrent, GenomeVariation as GenomeVariationCurrent, \
    Organism as OrganismCurrent, OrganismAlias as OrganismAliasCurrent, OrganismPublication as OrganismPublicationCurrent

from metadata_registry.models.assembly import Assembly, AssemblySequence
from metadata_registry.models.compara import ComparaAnalysis, ComparaAnalysisEvent
from metadata_registry.models.datarelease import DataRelease, EnsemblSite
from metadata_registry.models.division import Division
from metadata_registry.models.genomeinfo import Genome, GenomeAlignment, GenomeAnnotation, GenomeComparaAnalysis, \
    GenomeDatabase, GenomeEvent, GenomeFeature, GenomeVariation, GenomeRelease, GenomeDivision
from metadata_registry.models.organism import Organism, OrganismAlias, OrganismPublication, OrganismGroup
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Migrate data from previous Ensembl Metadata schema version'

    def add_arguments(self, parser):
        parser.add_argument('-r', '--releases', type=str, required=False,
                            help='Ensembl release number(s) - format: XX, -XX, XX-, XX-YY')
        parser.add_argument('-s', '--site', type=str, required=False, default='Ensembl',
                            help='Ensembl release number(s) - format: XX, -XX, XX-, XX-YY')
        parser.add_argument('--eg', type=bool, action='store', required=False, default=0,
                            help='use EG release instead of Ensembl')

    def handle(self, *args, **options):
        site = options['site']

        # 96 import 96
        # 96, import 96 and latest releases
        # ,96 import earliest releases up to 96
        # 96,98 import releases between 96 and 98
        release = options['releases']
        release_list = []
        # Use EG release ensembl_genomes_version, else use ensembl_version
        # Use EG=1 for RR or sister projects of ensembl
        eg = options['eg']

        # Dealing with Ensembl Site
        NewEnsemblSite = EnsemblSite()

        if site == 'RR':
            # For Rapid Release
            NewEnsemblSite.label = 'Rapid Release'
            NewEnsemblSite.uri = 'https://rapid.ensembl.org/index.html'
        else:
            NewEnsemblSite.label = 'Ensembl Release'
            NewEnsemblSite.uri = 'https://www.ensembl.org/index.html'

        NewEnsemblSite.save()

        # Dealing with data release
        if release:
            # Range from 96 to latest release (96,)
            if release.endswith(','):
                if eg:
                    Releases = DataReleaseCurrent.objects.filter(ensembl_genomes_version__gte=release[:-1])
                else:
                    Releases = DataReleaseCurrent.objects.filter(ensembl_version__gte=release[:-1])
            # Range from earliest to 96 (,96)
            elif release.startswith(','):
                if eg:
                    Releases = DataReleaseCurrent.objects.filter(ensembl_genomes_version__lte=release[1:])
                else:
                    Releases = DataReleaseCurrent.objects.filter(ensembl_version__lte=release[1:])
            # Range between two releases 96 and 98 (96,98)
            elif ',' in release:
                rel = release.split(',')
                if eg:
                    Releases = DataReleaseCurrent.objects.filter(ensembl_genomes_version__range=(rel[0], rel[1]))
                else:
                    Releases = DataReleaseCurrent.objects.filter(ensembl_version__range=(rel[0], rel[1]))
            else:
                if eg:
                    Releases = DataReleaseCurrent.objects.filter(ensembl_genomes_version=release)
                else:
                    Releases = DataReleaseCurrent.objects.filter(ensembl_version=release)
        else:
            Releases = DataReleaseCurrent.objects.all()
        for DataReleaseCurr in Releases:
            release_list.append(DataReleaseCurr.data_release_id)
            NewDataRelease = DataRelease()
            if eg:
                # For Rapid Release and before unified releases
                NewDataRelease.version = DataReleaseCurr.ensembl_genomes_version
            else:
                # For Main release
                NewDataRelease.version = DataReleaseCurr.ensembl_version
            if DataReleaseCurr.ensembl_genomes_version is None:
                NewDataRelease.label = 'Vert only'
            NewDataRelease.release_date = DataReleaseCurr.release_date
            NewDataRelease.is_current = DataReleaseCurr.is_current
            NewDataRelease.data_release_id = DataReleaseCurr.data_release_id
            NewDataRelease.site_id = NewEnsemblSite.site_id
            NewDataRelease.save()

        # Populating division table
        DivisionCurr = DivisionCurrent.objects.all()
        Division.objects.bulk_create(DivisionCurr)

        # Dealing with Compara table
        ComparaAnalysisCurr = ComparaAnalysisCurrent.objects.filter(data_release_id__in=release_list)
        ComparaAnalysis.objects.bulk_create(ComparaAnalysisCurr)
        ComparaAnalysisEventCurr = ComparaAnalysisEventCurrent.objects.filter(
            compara_analysis_id__in=ComparaAnalysisCurr)
        ComparaAnalysisEvent.objects.bulk_create(ComparaAnalysisEventCurr)

        # Populating Genome table and associated genome_* tables
        for GenomeCurr in GenomeCurrent.objects.filter(data_release_id__in=release_list):
            NewGenome = Genome()
            NewGenome.genome_id = GenomeCurr.genome_id
            NewGenome.genebuild = GenomeCurr.genebuild
            NewGenome.has_pan_compara = GenomeCurr.has_pan_compara
            NewGenome.has_variation = GenomeCurr.has_variations
            NewGenome.has_microarray = GenomeCurr.has_microarray
            NewGenome.has_peptide_compara = GenomeCurr.has_peptide_compara
            NewGenome.has_genome_alignments = GenomeCurr.has_genome_alignments
            NewGenome.has_synteny = GenomeCurr.has_synteny
            NewGenome.has_other_alignments = GenomeCurr.has_other_alignments
            NewGenome.created = GenomeEventCurrent.objects.filter(genome_id=NewGenome.genome_id).last().creation_time
            # Dealing with Organism, Organism_alias and organism_publcation tables
            OrganismCurr = OrganismCurrent.objects.filter(organism_id=GenomeCurr.organism_id).first()
            NewOrganism = Organism()
            NewOrganism.organism_id = OrganismCurr.organism_id
            NewOrganism.taxonomy_id = OrganismCurr.taxonomy_id
            NewOrganism.reference = OrganismCurr.reference
            NewOrganism.species_taxonomy_id = OrganismCurr.species_taxonomy_id
            NewOrganism.name = OrganismCurr.name
            NewOrganism.display_name = OrganismCurr.display_name
            NewOrganism.strain = OrganismCurr.strain
            NewOrganism.serotype = OrganismCurr.serotype
            NewOrganism.description = OrganismCurr.description
            NewOrganism.image = OrganismCurr.image
            NewOrganism.scientific_name = OrganismCurr.scientific_name
            NewOrganism.url_name = OrganismCurr.url_name
            # Populating new group table
            NewOrganismGroup = OrganismGroup()
            NewOrganismGroup.type = 'strains'
            NewOrganismGroup.reference_organism = Organism.objects.filter(name=OrganismCurr.reference).first()
            NewOrganismGroup.save()
            NewOrganism.group = NewOrganismGroup
            NewOrganism.save()
            # Deal with organism Alias
            OrganismAliasCurr = OrganismAliasCurrent.objects.filter(organism_id=NewOrganism.organism_id)
            OrganismAlias.objects.bulk_create(OrganismAliasCurr)
            # Deal with organim publication
            OrganismPublicationCurr = OrganismPublicationCurrent.objects.filter(organism_id=NewOrganism.organism_id)
            OrganismPublication.objects.bulk_create(OrganismPublicationCurr)
            NewGenome.organism = NewOrganism
            # Dealing with Assembly table
            # Populating AssemblySequence table is time consuming so better check if data exist first
            # Since it's shared between releases
            CheckAssemblyExist = Assembly.objects.filter(assembly_id=GenomeCurr.assembly_id)
            if CheckAssemblyExist.count() == 0:
                AssemblyCurr = AssemblyCurrent.objects.filter(assembly_id=GenomeCurr.assembly_id).first()
                NewAssembly = Assembly()
                NewAssembly.assembly_id = AssemblyCurr.assembly_id
                NewAssembly.assembly_accession = AssemblyCurr.assembly_accession
                NewAssembly.assembly_name = AssemblyCurr.assembly_name
                NewAssembly.assembly_default = AssemblyCurr.assembly_default
                NewAssembly.assembly_ucsc = AssemblyCurr.assembly_ucsc
                NewAssembly.assembly_level = AssemblyCurr.assembly_level
                NewAssembly.base_count = AssemblyCurr.base_count
                NewAssembly.save()
                # Dealing with Assembly sequence table
                batch_size = 10000
                AssemblySequenceCurr = AssemblySequenceCurrent.objects.filter(assembly_id=AssemblyCurr.assembly_id)
                AssemblySequence.objects.bulk_create(AssemblySequenceCurr, batch_size)
                NewGenome.assembly = NewAssembly
                NewGenome.save()
            else:
                NewGenome.assembly = CheckAssemblyExist.first()
                NewGenome.save()
            # Dealing with Genome databases
            GenomeDatabaseCurr = GenomeDatabaseCurrent.objects.filter(genome_id=NewGenome.genome_id)
            GenomeDatabase.objects.bulk_create(GenomeDatabaseCurr)
            # Dealing with Genome alignement
            GenomeAlignmentCurr = GenomeAlignmentCurrent.objects.filter(genome_id=NewGenome.genome_id)
            GenomeAlignment.objects.bulk_create(GenomeAlignmentCurr)
            # Dealing with Genome annotation
            GenomeAnnotationCurr = GenomeAnnotationCurrent.objects.filter(genome_id=NewGenome.genome_id)
            GenomeAnnotation.objects.bulk_create(GenomeAnnotationCurr)
            # Dealing with Genome Features
            GenomeFeatureCurr = GenomeFeatureCurrent.objects.filter(genome_id=NewGenome.genome_id)
            GenomeFeature.objects.bulk_create(GenomeFeatureCurr)
            # Dealing with Genome Variation
            GenomeVariationCurr = GenomeVariationCurrent.objects.filter(genome_id=NewGenome.genome_id)
            GenomeVariation.objects.bulk_create(GenomeVariationCurr)
            # Dealing with Genome Compara analysis
            GenomeComparaAnalysisCurr = GenomeComparaAnalysisCurrent.objects.filter(genome_id=NewGenome.genome_id)
            GenomeComparaAnalysis.objects.bulk_create(GenomeComparaAnalysisCurr)
            # Dealing with Genome Event
            GenomeEventCurr = GenomeEventCurrent.objects.filter(genome_id=NewGenome.genome_id)
            GenomeEvent.objects.bulk_create(GenomeEventCurr)
            # Populating division table
            DivisionCurr = DivisionCurrent.objects.filter(division_id=GenomeCurr.division_id).first()
            NewDivision = Division()
            NewDivision.division_id = DivisionCurr.division_id
            NewDivision.name = DivisionCurr.name
            NewDivision.short_name = DivisionCurr.short_name
            NewDivision.save()
            # Dealing with new Genome Division table
            NewGenomeDivision = GenomeDivision()
            NewGenomeDivision.division = Division.objects.filter(division_id=GenomeCurr.division_id).first()
            NewGenomeDivision.genome = NewGenome
            NewGenomeDivision.save()
            # Dealing with new Genome Release table
            NewGenomeRelease = GenomeRelease()
            NewGenomeRelease.genome_uuid = NewGenome
            NewGenomeRelease.division = Division.objects.filter(division_id=GenomeCurr.division_id).first()
            NewGenomeRelease.data_release = DataRelease.objects.filter(
                data_release_id=GenomeCurr.data_release_id).first()
            NewGenomeRelease.save()
