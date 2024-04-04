from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination as BasePageNumberPagination


class CustomPageNumberPagination(BasePageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'limit'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))
