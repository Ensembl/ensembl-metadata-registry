from rest_framework.filters import BaseFilterBackend
from ncbi_taxonomy.api.utils import TaxonomyUtils


class TaxonomyFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        taxon_ids_string = request.query_params.get('taxon_ids', None)
        if taxon_ids_string is not None:
            if request.query_params.get('descendents'):
                taxon_ids = TaxonomyUtils.fetch_descendent_ids(taxon_ids_string)
            else:
                taxon_ids = [int(x.strip()) for x in taxon_ids_string.split(',')]
            queryset = queryset.filter(taxon_id__in=taxon_ids)

        return queryset.order_by('taxon_id')

    def get_schema_operation_parameters(self, view):
        return [
            {
                'name': 'taxon_ids',
                'description': 'Comma-separated taxon ids (e.g. 9606,10090)',
                'required': False,
                'in': 'query',
                'schema': {
                    'type': 'string',
                },
            },
            {
                'name': 'descendents',
                'description': 'Include descendent taxonomic entries',
                'required': False,
                'in': 'query',
                'schema': {
                    'type': 'boolean',
                },
            },
        ]
