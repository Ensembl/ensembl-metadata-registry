from django.conf import settings

from metadata_orm.models import \
    Assembly as AssemblyCurrent, \
    AssemblySequence as AssemblySequenceCurrent, \
    ComparaAnalysis as ComparaAnalysisCurrent, \
    ComparaAnalysisEvent as ComparaAnalysisEventCurrent, \
    DataRelease as DataReleaseCurrent, Division as DivisionCurrent, \
    Genome as GenomeCurrent, \
    GenomeAlignment as GenomeAlignmentCurrent, \
    GenomeAnnotation as GenomeAnnotationCurrent, \
    GenomeComparaAnalysis as GenomeComparaAnalysisCurrent, \
    GenomeDatabase as GenomeDatabaseCurrent, \
    GenomeEvent as GenomeEventCurrent, \
    GenomeFeature as GenomeFeatureCurrent, \
    GenomeVariation as GenomeVariationCurrent, \
    Organism as OrganismCurrent, \
    OrganismAlias as OrganismAliasCurrent, \
    OrganismPublication as OrganismPublicationCurrent

from ensembl_metadata.models.assembly import \
    Assembly, \
    AssemblySequence
from ensembl_metadata.models.compara import \
    ComparaAnalysis, \
    ComparaAnalysisEvent
from ensembl_metadata.models.datarelease import \
    DataRelease, \
    Division, \
    EnsemblSite
from ensembl_metadata.models.genome import \
    Genome, \
    GenomeAlignment, \
    GenomeAnnotation, \
    GenomeComparaAnalysis, \
    GenomeDatabase, \
    GenomeEvent, \
    GenomeFeature, \
    GenomeVariation, \
    GenomeRelease, \
    GenomeDivision
from ensembl_metadata.models.organism import \
    Organism, \
    OrganismAlias, \
    OrganismPublication, \
    OrganismGroup
from django.core.management.base import BaseCommand

"""
This script is intended to allow migration from pre-2020-site
ensembl_metadata schema to the new schema.
"""


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
        new_ensembl_site = EnsemblSite()

        if site == 'RR':
            # For Rapid Release
            new_ensembl_site.label = 'Rapid Release'
            new_ensembl_site.uri = 'https://rapid.ensembl.org/index.html'
        else:
            new_ensembl_site.label = 'Ensembl Release'
            new_ensembl_site.uri = 'https://www.ensembl.org/index.html'

        new_ensembl_site.save()

        # Dealing with data release
        if release:
            # Range from 96 to latest release (96,)
            if release.endswith(','):
                if eg:
                    releases = DataReleaseCurrent.objects.filter(ensembl_genomes_version__gte=release[:-1])
                else:
                    releases = DataReleaseCurrent.objects.filter(ensembl_version__gte=release[:-1])
            # Range from earliest to 96 (,96)
            elif release.startswith(','):
                if eg:
                    releases = DataReleaseCurrent.objects.filter(ensembl_genomes_version__lte=release[1:])
                else:
                    releases = DataReleaseCurrent.objects.filter(ensembl_version__lte=release[1:])
            # Range between two releases 96 and 98 (96,98)
            elif ',' in release:
                rel = release.split(',')
                if eg:
                    releases = DataReleaseCurrent.objects.filter(ensembl_genomes_version__range=(rel[0], rel[1]))
                else:
                    releases = DataReleaseCurrent.objects.filter(ensembl_version__range=(rel[0], rel[1]))
            else:
                if eg:
                    releases = DataReleaseCurrent.objects.filter(ensembl_genomes_version=release)
                else:
                    releases = DataReleaseCurrent.objects.filter(ensembl_version=release)
        else:
            releases = DataReleaseCurrent.objects.all()
        for DataReleaseCurr in releases:
            release_list.append(DataReleaseCurr.data_release_id)
            new_data_release = DataRelease()
            if eg:
                # For Rapid Release and before unified releases
                new_data_release.version = DataReleaseCurr.ensembl_genomes_version
            else:
                # For Main release
                new_data_release.version = DataReleaseCurr.ensembl_version
            if DataReleaseCurr.ensembl_genomes_version is None:
                new_data_release.label = 'Vert only'
            new_data_release.release_date = DataReleaseCurr.release_date
            new_data_release.is_current = DataReleaseCurr.is_current
            new_data_release.data_release_id = DataReleaseCurr.data_release_id
            new_data_release.site_id = new_ensembl_site.site_id
            new_data_release.save()

        # Populating division table
        division_curr = DivisionCurrent.objects.all()
        Division.objects.bulk_create(division_curr)

        # Dealing with Compara table
        compara_analysis_curr = ComparaAnalysisCurrent.objects.filter(data_release_id__in=release_list)
        ComparaAnalysis.objects.bulk_create(compara_analysis_curr)
        compara_analysis_event_curr = ComparaAnalysisEventCurrent.objects.filter(
            compara_analysis_id__in=compara_analysis_curr)
        ComparaAnalysisEvent.objects.bulk_create(compara_analysis_event_curr)

        # Populating Genome table and associated genome_* tables
        for genome_curr in GenomeCurrent.objects.filter(data_release_id__in=release_list):
            new_genome = Genome()
            new_genome.genome_id = genome_curr.genome_id
            new_genome.genebuild = genome_curr.genebuild
            new_genome.has_pan_compara = genome_curr.has_pan_compara
            new_genome.has_variation = genome_curr.has_variations
            new_genome.has_microarray = genome_curr.has_microarray
            new_genome.has_peptide_compara = genome_curr.has_peptide_compara
            new_genome.has_genome_alignments = genome_curr.has_genome_alignments
            new_genome.has_synteny = genome_curr.has_synteny
            new_genome.has_other_alignments = genome_curr.has_other_alignments
            new_genome.created = GenomeEventCurrent.objects.filter(genome_id=new_genome.genome_id).last().creation_time
            # Dealing with Organism, Organism_alias and organism_publication tables
            organism_curr = OrganismCurrent.objects.filter(organism_id=genome_curr.organism_id).first()
            new_organism = Organism()
            new_organism.organism_id = organism_curr.organism_id
            new_organism.taxonomy_id = organism_curr.taxonomy_id
            new_organism.reference = organism_curr.reference
            new_organism.species_taxonomy_id = organism_curr.species_taxonomy_id
            new_organism.name = organism_curr.name
            new_organism.display_name = organism_curr.display_name
            new_organism.strain = organism_curr.strain
            new_organism.serotype = organism_curr.serotype
            new_organism.description = organism_curr.description
            new_organism.image = organism_curr.image
            new_organism.scientific_name = organism_curr.scientific_name
            new_organism.url_name = organism_curr.url_name
            # Populating new group table
            new_organism_group = OrganismGroup()
            new_organism_group.type = 'strains'
            new_organism_group.reference_organism = Organism.objects.filter(name=organism_curr.reference).first()
            new_organism_group.save()
            new_organism.organism_group = new_organism_group
            new_organism.save()
            # Deal with organism Alias
            organism_alias_curr = OrganismAliasCurrent.objects.filter(organism_id=new_organism.organism_id)
            OrganismAlias.objects.bulk_create(organism_alias_curr, ignore_conflicts=True)
            # Deal with organism publication
            organism_publication_curr = OrganismPublicationCurrent.objects.filter(organism_id=new_organism.organism_id)
            OrganismPublication.objects.bulk_create(organism_publication_curr)
            new_genome.organism = new_organism
            # Dealing with Assembly table
            # Populating AssemblySequence table is time consuming so better check if data exist first
            # Since it's shared between releases
            check_assembly_exist = Assembly.objects.filter(assembly_id=genome_curr.assembly_id)
            if check_assembly_exist.count() == 0:
                assembly_curr = AssemblyCurrent.objects.filter(assembly_id=genome_curr.assembly_id).first()
                new_assembly = Assembly()
                new_assembly.assembly_id = assembly_curr.assembly_id
                new_assembly.assembly_accession = assembly_curr.assembly_accession
                new_assembly.assembly_name = assembly_curr.assembly_name
                new_assembly.assembly_default = assembly_curr.assembly_default
                new_assembly.assembly_ucsc = assembly_curr.assembly_ucsc
                new_assembly.assembly_level = assembly_curr.assembly_level
                new_assembly.base_count = assembly_curr.base_count
                new_assembly.save()
                # Dealing with Assembly sequence table
                batch_size = 10000
                assembly_sequence_curr = AssemblySequenceCurrent.objects.filter(assembly_id=assembly_curr.assembly_id)
                AssemblySequence.objects.bulk_create(assembly_sequence_curr, batch_size)
                new_genome.assembly = new_assembly
                new_genome.save()
            else:
                new_genome.assembly = check_assembly_exist.first()
                new_genome.save()
            # Dealing with Genome databases
            genome_database_curr = GenomeDatabaseCurrent.objects.filter(genome_id=new_genome.genome_id)
            GenomeDatabase.objects.bulk_create(genome_database_curr)
            # Dealing with Genome alignment
            genome_alignment_curr = GenomeAlignmentCurrent.objects.filter(genome_id=new_genome.genome_id)
            GenomeAlignment.objects.bulk_create(genome_alignment_curr)
            # Dealing with Genome annotation
            genome_annotation_curr = GenomeAnnotationCurrent.objects.filter(genome_id=new_genome.genome_id)
            GenomeAnnotation.objects.bulk_create(genome_annotation_curr)
            # Dealing with Genome Features
            genome_feature_curr = GenomeFeatureCurrent.objects.filter(genome_id=new_genome.genome_id)
            GenomeFeature.objects.bulk_create(genome_feature_curr)
            # Dealing with Genome Variation
            genome_variation_curr = GenomeVariationCurrent.objects.filter(genome_id=new_genome.genome_id)
            GenomeVariation.objects.bulk_create(genome_variation_curr)
            # Dealing with Genome Compara analysis
            genome_compara_analysis_curr = GenomeComparaAnalysisCurrent.objects.filter(genome_id=new_genome.genome_id)
            GenomeComparaAnalysis.objects.bulk_create(genome_compara_analysis_curr)
            # Dealing with Genome Event
            genome_event_curr = GenomeEventCurrent.objects.filter(genome_id=new_genome.genome_id)
            GenomeEvent.objects.bulk_create(genome_event_curr)
            # Populating division table
            division_curr = DivisionCurrent.objects.filter(division_id=genome_curr.division_id).first()
            new_division = Division()
            new_division.division_id = division_curr.division_id
            new_division.name = division_curr.name
            new_division.short_name = division_curr.short_name
            new_division.save()
            # Dealing with new Genome Division table
            new_genome_division = GenomeDivision()
            new_genome_division.division = Division.objects.filter(division_id=genome_curr.division_id).first()
            new_genome_division.genome = new_genome
            new_genome_division.save()
            # Dealing with new Genome Release table
            new_genome_release = GenomeRelease()
            new_genome_release.genome_uuid = new_genome
            new_genome_release.division = Division.objects.filter(division_id=genome_curr.division_id).first()
            new_genome_release.data_release = DataRelease.objects.filter(
                data_release_id=genome_curr.data_release_id).first()
            new_genome_release.save()
