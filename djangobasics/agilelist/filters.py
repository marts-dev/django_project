import django_filters
from agilelist.models import Statement


class StatementFilter(django_filters.FilterSet):
    class Meta:
        model = Statement
        fields = {"title": ["icontains"], "category": ["exact"]}
