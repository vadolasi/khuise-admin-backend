import django_filters
from django_filters import filters

from apps.products import models


class ProductFilter(django_filters.FilterSet):
    categories = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Product
        fields = {
            'name': ['icontains'],
            'price': ['lt', 'gt'],
        }
