from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination


class NoPagination(LimitOffsetPagination):
    default_limit = None
    max_limit = None


class ElibraryCommonPaginator(PageNumberPagination):
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 100
