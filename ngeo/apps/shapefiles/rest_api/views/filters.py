import django_filters
from ...models import SubLocation, IsioloProject

class SublocationFilter(django_filters.FilterSet):
    locname = django_filters.CharFilter(lookup_expr='iexact')
    sub_name = django_filters.CharFilter(lookup_expr='iexact')
    divname = django_filters.CharFilter(lookup_expr='iexact')
    distname = django_filters.CharFilter(lookup_expr='iexact')
    provname = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = SubLocation
        fields = {
            'locname': ['iexact', ],
            'sub_name': ['iexact', ],
            
        }

class ProjectFilter(django_filters.FilterSet):
    theme = django_filters.CharFilter(lookup_expr='iexact')
    fname = django_filters.CharFilter(lookup_expr='iexact')
    id = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = IsioloProject
        fields = ['fname', 'theme']