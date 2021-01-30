from django_filters import FilterSet

from .models import Spread, Future


class SpreadFilterSet(FilterSet):
    class Meta:
        model = Spread
        fields = {
            'pair_a': ['exact'],
            'pair_b': ['exact'],
            'created_at': ['exact', 'gt', 'gte', 'lt', 'lte'],
        }


class FutureFilterSet(FilterSet):
    class Meta:
        model = Future
        fields = {
            'id': ['exact'],
            'name': ['exact'],
        }