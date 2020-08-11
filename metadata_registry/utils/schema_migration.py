from metadata_registry.models.assembly import Assembly, AssemblySequence
from metadata_registry_current.models.assembly import Assembly as AssemblyCurrent, AssemblySequence as AssemblySequenceCurrent
from metadata_registry.models.compara import ComparaAnalysis, ComparaAnalysisEvent
from metadata_registry_current.models.compara import ComparaAnalysis as ComparaAnalysisCurrent, ComparaAnalysisEvent as ComparaAnalysisEventCurrent
from metadata_registry.models.datarelease import DataRelease, EnsemblSite
from metadata_registry_current.models.datarelease import DataRelease as DataReleaseCurrent
from metadata_registry.models.organism import Organism, OrganismAlias, OrganismPublication, OrganismGroup
from metadata_registry_current.models.organism import Organism as OrganismCurrent, OrganismAlias as OrganismAliasCurrent, OrganismPublication as OrganismPublicationCurrent
from metadata_registry.models.division import Division
from metadata_registry_current.models.division import Division as DivisionCurrent
from metadata_registry.models.genomeinfo import Genome, GenomeAlignment, GenomeAnnotation, GenomeComparaAnalysis, GenomeDatabase, GenomeEvent, GenomeFeature, GenomeVariation, GenomeRelease, GenomeDivision 
from metadata_registry_current.models.genomeinfo import Genome as GenomeCurrent, GenomeAlignment as GenomeAlignmentCurrent, GenomeAnnotation as GenomeAnnotationCurrent, GenomeComparaAnalysis as GenomeComparaAnalysisCurrent, GenomeDatabase as GenomeDatabaseCurrent, GenomeEvent as GenomeEventCurrent, GenomeFeature as GenomeFeatureCurrent, GenomeVariation as GenomeVariationCurrent

site='RR'
# Dealing with Assembly table
#for AssemblyCurr in AssemblyCurrent.objects.all():
#    NewAssembly=Assembly()
#    NewAssembly.assembly_id=AssemblyCurr.assembly_id
#    NewAssembly.assembly_accession=AssemblyCurr.assembly_accession
#    NewAssembly.assembly_name=AssemblyCurr.assembly_name
#    NewAssembly.assembly_default=AssemblyCurr.assembly_default
#    NewAssembly.assembly_ucsc=AssemblyCurr.assembly_ucsc
#    NewAssembly.assembly_level=AssemblyCurr.assembly_level
#    NewAssembly.base_count=AssemblyCurr.base_count
#    NewAssembly.save()

# Dealing with Assembly sequence table
#for AssemblySequenceCurr in AssemblySequenceCurrent.objects.all():
#    NewAssemblySequence=AssemblySequence()
#    NewAssemblySequence.assembly_sequence_id=AssemblySequenceCurr.assembly_sequence_id
#    NewAssemblySequence.assembly_id=AssemblySequenceCurr.assembly_id
#    NewAssemblySequence.name=AssemblySequenceCurr.name
#    NewAssemblySequence.acc=AssemblySequenceCurr.acc
#    NewAssemblySequence.save()

# Dealing with Compara table
for ComparaAnalysisCurr in ComparaAnalysisCurrent.objects.all():
    NewComparaAnalysis=ComparaAnalysis()
    NewComparaAnalysis.compara_analysis_id=ComparaAnalysisCurr.analysis_id
    NewComparaAnalysis.data_release_id=ComparaAnalysisCurr.data_release_id
    NewComparaAnalysis.division_id=ComparaAnalysisCurr.division_id
    NewComparaAnalysis.method=ComparaAnalysisCurr.method
    NewComparaAnalysis.set_name=ComparaAnalysisCurr.set_name
    NewComparaAnalysis.dbname=ComparaAnalysisCurr.dbname
    for ComparaAnalysisEventCurr in ComparaAnalysisEventCurrent.objects.all():
        NewComparaAnalysisEvent = ComparaAnalysisEvent()
        NewComparaAnalysisEvent.compara_analysis_event_id = ComparaAnalysisEventCurr.compara_analysis_event_id
        NewComparaAnalysisEvent.compara_analysis = ComparaAnalysisEventCurr.compara_analysis
        NewComparaAnalysisEvent.type = ComparaAnalysisEventCurr.type
        NewComparaAnalysisEvent.source = ComparaAnalysisEventCurr.source
        NewComparaAnalysisEvent.creation_time = ComparaAnalysisEventCurr.creation_time
        NewComparaAnalysisEvent.details = ComparaAnalysisEventCurr.details
    NewComparaAnalysis.save()
    NewComparaAnalysisEvent.save()

# Dealing with Ensembl Site
NewEnsemblSite=EnsemblSite()
if site == 'RR':
    # For Rapid Release
    NewEnsemblSite.label='Rapid Release'
    NewEnsemblSite.uri='https://rapid.ensembl.org/index.html'
else:
    NewEnsemblSite.label='Ensembl Release'
    NewEnsemblSite.uri='https://www.ensembl.org/index.html'
NewEnsemblSite.save()

# Dealing with data release
for DataReleaseCurr in DataReleaseCurrent.objects.all():
    NewDataRelease=DataRelease()
    if site=='RR':
        # For Rapid Release
        NewDataRelease.version=DataReleaseCurr.ensembl_genomes_version
    else:
        # For Main release
        NewDataRelease.version=DataReleaseCurr.ensembl_version
    NewDataRelease.release_date=DataReleaseCurr.release_date
    NewDataRelease.is_current=DataReleaseCurr.is_current
    NewDataRelease.data_release_id = DataReleaseCurr.data_release_id
    NewDataRelease.site_id=NewEnsemblSite.site_id
    NewDataRelease.save()

#Dealing with Organism, Organism_alias and organism_publcation tables
for OrganismCurr in OrganismCurrent.objects.all():
    NewOrganism=Organism()
    NewOrganism.organism_id = OrganismCurr.organism_id
    NewOrganism.taxonomy_id = OrganismCurr.taxonomy_id
    NewOrganism.reference =  OrganismCurr.reference
    NewOrganism.species_taxonomy_id = OrganismCurr.species_taxonomy_id
    NewOrganism.name = OrganismCurr.name
    NewOrganism.display_name = OrganismCurr.display_name
    NewOrganism.strain = OrganismCurr.strain
    NewOrganism.serotype = OrganismCurr.serotype
    NewOrganism.description = OrganismCurr.description
    NewOrganism.image = OrganismCurr.image
    NewOrganism.scientific_name = OrganismCurr.scientific_name
    NewOrganism.url_name = OrganismCurr.url_name
    NewOrganism.save()
    for OrganismAliasCurr in OrganismAliasCurrent.objects.filter(organism_id=NewOrganism.organism_id):
        NewOrganismAlias=OrganismAlias()
        NewOrganismAlias.organism_alias_id = OrganismAliasCurr.organism_alias_id
        NewOrganismAlias.organism = NewOrganism
        NewOrganismAlias.alias = OrganismAliasCurr.alias
        NewOrganismAlias.save()
    for OrganismPublicationCurr in OrganismPublicationCurrent.objects.filter(organism_id=NewOrganism.organism_id):
        NewOrganismPublication = OrganismPublication()
        NewOrganismPublication.organism_publication_id = OrganismPublicationCurr.organism_publication_id
        NewOrganismPublication.organism = NewOrganism
        NewOrganismPublication.publication = OrganismPublicationCurr.publication
        NewOrganismPublication.save()
    
# Populating new group table
for OrganismCurr in OrganismCurrent.objects.exclude(reference__isnull=True).exclude(reference=''):
    NewOrganismGroup=OrganismGroup()
    NewOrganismGroup.type='strains'
    NewOrganismGroup.reference_organism = Organism.objects.filter(name=OrganismCurr.reference).first()
    NewOrganismGroup.save()
    NewOrganism = Organism.objects.filter(organism_id=OrganismCurr.organism_id).first()
    NewOrganism.group = NewOrganismGroup
    NewOrganism.save()
    
# Populating division table
for DivisionCurr in DivisionCurrent.objects.all():
    NewDivision=Division()
    NewDivision.division_id = DivisionCurr.division_id
    NewDivision.name = DivisionCurr.name
    NewDivision.short_name = DivisionCurr.short_name
    NewDivision.save()
    
# Populating Genome table and associated genome_* tables
for GenomeCurr in GenomeCurrent.objects.all():
    NewGenome=Genome()
    NewGenome.genome_id = GenomeCurr.genome_id
    NewGenome.assembly = Assembly.objects.filter(assembly_id=GenomeCurr.assembly_id).first()
    NewGenome.organism = Organism.objects.filter(organism_id=GenomeCurr.organism_id).first()
    NewGenome.genebuild = GenomeCurr.genebuild
    NewGenome.has_pan_compara = GenomeCurr.has_pan_compara
    NewGenome.has_variation = GenomeCurr.has_variations
    #NewGenome.has_microarray = GenomeCurr.has_microarray
    NewGenome.has_microarray=0
    NewGenome.has_peptide_compara = GenomeCurr.has_peptide_compara
    NewGenome.has_genome_alignments = GenomeCurr.has_genome_alignments
    NewGenome.has_synteny = GenomeCurr.has_synteny
    NewGenome.has_other_alignments = GenomeCurr.has_other_alignments
    NewGenome.created = GenomeEventCurrent.objects.filter(genome_id=NewGenome.genome_id).last().creation_time
    NewGenome.save()
    for GenomeDatabaseCurr in GenomeDatabaseCurrent.objects.filter(genome_id=NewGenome.genome_id):
        NewGenomeDatabase = GenomeDatabase()
        NewGenomeDatabase.genome_database_id = GenomeDatabaseCurr.genome_database_id
        NewGenomeDatabase.genome = NewGenome
        NewGenomeDatabase.dbname = GenomeDatabaseCurr.dbname
        NewGenomeDatabase.species_id = GenomeDatabaseCurr.species_id
        NewGenomeDatabase.type = GenomeDatabaseCurr.type
        NewGenomeDatabase.save()
        for GenomeAlignmentCurr in GenomeAlignmentCurrent.objects.filter(genome_id=NewGenome.genome_id):
            MewGenomeAlignment = GenomeAlignment()
            MewGenomeAlignment.genome_alignment_id = GenomeAlignmentCurr.genome_alignment_id
            MewGenomeAlignment.genome = NewGenome
            MewGenomeAlignment.type = GenomeAlignmentCurr.type
            MewGenomeAlignment.name = GenomeAlignmentCurr.name
            MewGenomeAlignment.count = GenomeAlignmentCurr.count
            MewGenomeAlignment.genome_database = NewGenomeDatabase
            MewGenomeAlignment.save()
        for GenomeAnnotationCurr in GenomeAnnotationCurrent.objects.filter(genome_id=NewGenome.genome_id):
            NewGenomeAnnotation = GenomeAnnotation()
            NewGenomeAnnotation.genome_annotation_id = GenomeAnnotationCurr.genome_annotation_id
            NewGenomeAnnotation.genome = NewGenome
            NewGenomeAnnotation.type = GenomeAnnotationCurr.type
            NewGenomeAnnotation.value = GenomeAnnotationCurr.value
            NewGenomeAnnotation.genome_database = NewGenomeDatabase
            NewGenomeAnnotation.save()
        for GenomeFeatureCurr in GenomeFeatureCurrent.objects.filter(genome_id=NewGenome.genome_id):
            NewGenomeFeature = GenomeFeature()
            NewGenomeFeature.genome_feature_id = GenomeFeatureCurr.genome_feature_id
            NewGenomeFeature.genome = NewGenome
            NewGenomeFeature.type = GenomeFeatureCurr.type
            NewGenomeFeature.analysis = GenomeFeatureCurr.analysis
            NewGenomeFeature.count = GenomeFeatureCurr.count
            NewGenomeFeature.genome_database = NewGenomeDatabase
            NewGenomeFeature.save()
        for GenomeVariationCurr in GenomeVariationCurrent.objects.filter(genome_id=NewGenome.genome_id):
            NewGenomeVariation = GenomeVariation()
            NewGenomeVariation.genome_variation_id = GenomeVariationCurr.genome_variation_id
            NewGenomeVariation.genome = NewGenome
            NewGenomeVariation.type = GenomeVariationCurr.type
            NewGenomeVariation.name = GenomeVariationCurr.name
            NewGenomeVariation.count = GenomeVariationCurr.count
            NewGenomeVariation.genome_database = NewGenomeDatabase
            NewGenomeVariation.save()
    for GenomeComparaAnalysisCurr in GenomeComparaAnalysisCurrent.objects.filter(genome_id=NewGenome.genome_id):
        NewGenomeComparaAnalysis = GenomeComparaAnalysis()
        NewGenomeComparaAnalysis.genome_compara_analysis_id = GenomeComparaAnalysisCurr.genome_compara_analysis_id
        NewGenomeComparaAnalysis.genome = NewGenome
        NewGenomeComparaAnalysis.compara_analysis = GenomeComparaAnalysisCurr.compara_analysis
        NewGenomeComparaAnalysis.save()
    for GenomeEventCurr in GenomeEventCurrent.objects.filter(genome_id=NewGenome.genome_id):
        NewGenomeEvent = GenomeEvent()
        NewGenomeEvent.genome = NewGenome
        NewGenomeEvent.type = GenomeEventCurr.type
        NewGenomeEvent.source = GenomeEventCurr.source
        NewGenomeEvent.creation_time = GenomeEventCurr.creation_time
        NewGenomeEvent.details = GenomeEventCurr.details
        NewGenomeEvent.save()
    # Dealing with new Genome Division table
    NewGenomeDivision = GenomeDivision()
    NewGenomeDivision.division = Division.objects.filter(division_id=GenomeCurr.division_id).first()
    NewGenomeDivision.genome = NewGenome
    NewGenomeDivision.save()
    # Dealing with new Genome Release table
    NewGenomeRelease = GenomeRelease()
    NewGenomeRelease.genome_uuid = NewGenome
    NewGenomeRelease.division = Division.objects.filter(division_id=GenomeCurr.division_id).first()
    NewGenomeRelease.data_release = DataRelease.objects.filter(data_release_id=GenomeCurr.data_release_id).first()
    NewGenomeRelease.save()
