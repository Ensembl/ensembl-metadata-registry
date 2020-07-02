Metadata schema updated schema for 2020 Websites (and others concerns)
======================================================================


Examples
--------
Genome_variation dataset
````
[
  {
    "dbname": "oryza_sativa_variation_47_100_7", # issued from genome_database table
    "genome_variation_id": 79348, # internal id 
    "genome_id": 882509, # related Genome (unique per release for now)
    "type": "variations", # type of dataset
    "name": "EVA", # Source of variation set
    "count": 28179246, # count variations
    "genome_database_id": 1202206 # related database internal  id
  },
  {
    "dbname": "oryza_sativa_variation_47_100_7",
    "genome_variation_id": 79349,
    "genome_id": 882509,
    "type": "structuralVariations",
    "name": "gramene-marker",
    "count": 1278,
    "genome_database_id": 1202206
  }
]
````

Genome Feature dataset

````
[
  {
    "dbname": "oryza_sativa_core_47_100_7", # Original Core DB issued from genome_database table
    "genome_feature_id": 1321431, # Internal ID
    "genome_id": 882509, # related Genome (unique per release for now)
    "type": "repeatFeatures", # type of dataset
    "analysis": "dust", # Analysis description logic_name e.g associated track ?
    "count": 643631, # count features
    "genome_database_id": 1145572 # related database id
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_feature_id": 1321430,
    "genome_id": 882509,
    "type": "repeatFeatures",
    "analysis": "repeatmaskagi",
    "count": 389462,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_feature_id": 1321429,
    "genome_id": 882509,
    "type": "repeatFeatures",
    "analysis": "repeatmask_redat",
    "count": 246658,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_feature_id": 1321428,
    "genome_id": 882509,
    "type": "repeatFeatures",
    "analysis": "repeatmask_repbase",
    "count": 338391,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_feature_id": 1321432,
    "genome_id": 882509,
    "type": "repeatFeatures",
    "analysis": "trf",
    "count": 202751,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_feature_id": 1321433,
    "genome_id": 882509,
    "type": "simpleFeatures",
    "analysis": "ena_exon",
    "count": 44,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_feature_id": 1321435,
    "genome_id": 882509,
    "type": "simpleFeatures",
    "analysis": "ena_intron",
    "count": 10,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_feature_id": 1321434,
    "genome_id": 882509,
    "type": "simpleFeatures",
    "analysis": "ena_misc_feature",
    "count": 492,
    "genome_database_id": 1145572
  }
]
````

Genome_annotation
````
[
  {
    "dbname": "oryza_sativa_core_47_100_7", # Original Core DB issued from genome_database table
    "genome_annotation_id": 14510793, # Internal ID
    "genome_id": 882509, # related Genome (unique per release for now)
    "type": "genebuild_method", # Annotation method
    "value": "import", # Annotation type 
    "genome_database_id": 1145572 # related database id
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510784,
    "genome_id": 882509,
    "type": "nGO",
    "value": "22691",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510790,
    "genome_id": 882509,
    "type": "nInterPro",
    "value": "29212",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510783,
    "genome_id": 882509,
    "type": "nInterProDomains",
    "value": "174566",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510786,
    "genome_id": 882509,
    "type": "nProteinCoding",
    "value": "35775",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510795,
    "genome_id": 882509,
    "type": "nProteinCodingGO",
    "value": "22691",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510788,
    "genome_id": 882509,
    "type": "nProteinCodingInterPro",
    "value": "8375",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510785,
    "genome_id": 882509,
    "type": "nProteinCodingUniProtKB",
    "value": "35960",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510789,
    "genome_id": 882509,
    "type": "nProteinCodingUniProtKBSwissProt",
    "value": "3096",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510792,
    "genome_id": 882509,
    "type": "nProteinCodingUniProtKBTrEMBL",
    "value": "32864",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510794,
    "genome_id": 882509,
    "type": "nUniProtKBSwissProt",
    "value": "3080",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510791,
    "genome_id": 882509,
    "type": "nUniProtKBTrEMBL",
    "value": "36494",
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_annotation_id": 14510787,
    "genome_id": 882509,
    "type": "provider_name",
    "value": "RAP-DB",
    "genome_database_id": 1145572
  }
]
````

Genome Alignment

````
[
  {
    "dbname": "oryza_sativa_core_47_100_7", # Original Core DB issued from genome_database table
    "genome_alignment_id": 110021, # Internal ID
    "genome_id": 882509,  # related Genome (unique per release for now)
    "type": "bam", # format
    "name": "OsjapLeaf", # name (?)
    "count": 1, # original count
    "genome_database_id": 1145572 # related database id
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_alignment_id": 110020,
    "genome_id": 882509,
    "type": "bam",
    "name": "OsjapPanicle",
    "count": 1,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_alignment_id": 110019,
    "genome_id": 882509,
    "type": "bam",
    "name": "OsjapRoot",
    "count": 1,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_alignment_id": 110022,
    "genome_id": 882509,
    "type": "dnaAlignFeatures",
    "name": "cmscan_rfam_12.2_lca",
    "count": 3686,
    "genome_database_id": 1145572
  },
  {
    "dbname": "oryza_sativa_core_47_100_7",
    "genome_alignment_id": 110023,
    "genome_id": 882509,
    "type": "dnaAlignFeatures",
    "name": "trnascan_align",
    "count": 772,
    "genome_database_id": 1145572
  }
]
````

Compara Analysis

````
[
  {
    "dbname": "ensembl_compara_pan_homology_47_100", # Compara related DB
    "genome_compara_analysis_id": 259777, # Internal ID 
    "genome_id": 882509, # related Genome (unique per release for now)
    "compara_analysis_id": 31947, # Internal ID
    "data_release_id": 60, # Release
    "division_id": 7, # Associated division
    "method": "PROTEIN_TREES", # Compara analysis
    "set_name": "protein_tree_pan_eg46" # Question for Compara :-) (?)
  },
  {
    "dbname": "ensembl_compara_plants_47_100",
    "genome_compara_analysis_id": 259866,
    "genome_id": 882509,
    "compara_analysis_id": 31949,
    "data_release_id": 60,
    "division_id": 5,
    "method": "PROTEIN_TREES",
    "set_name": "plants protein-trees"
  },
  {
    "dbname": "ensembl_compara_plants_47_100",
    "genome_compara_analysis_id": 259905,
    "genome_id": 882509,
    "compara_analysis_id": 31954,
    "data_release_id": 60,
    "division_id": 5,
    "method": "LASTZ_NET",
    "set_name": "Osat-Tdic LastZ (on Osat)"
  },
  {
    "dbname": "ensembl_compara_plants_47_100",
    "genome_compara_analysis_id": 259915,
    "genome_id": 882509,
    "compara_analysis_id": 31959,
    "data_release_id": 60,
    "division_id": 5,
    "method": "LASTZ_NET",
    "set_name": "O.sat-H.ann lastz-net (on O.sat)"
  },
  {
    "dbname": "ensembl_compara_plants_47_100",
    "genome_compara_analysis_id": 259923,
    "genome_id": 882509,
    "compara_analysis_id": 31963,
    "data_release_id": 60,
    "division_id": 5,
    "method": "LASTZ_NET",
    "set_name": "Ccap-Osat LastZ (on Osat)"
  },
  {
    "dbname": "ensembl_compara_plants_47_100",
    "genome_compara_analysis_id": 259936,
    "genome_id": 882509,
    "compara_analysis_id": 31970,
    "data_release_id": 60,
    "division_id": 5,
    "method": "LASTZ_NET",
    "set_name": "T.ura-O.sat lastz_net"
  }
...

]
````
