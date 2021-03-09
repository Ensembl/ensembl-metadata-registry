from rest_framework.pagination import LimitOffsetPagination


class DataTablePagination(LimitOffsetPagination):
        limit_query_param = 'length'
        offset_query_param = 'start'
