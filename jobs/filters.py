from django_filters import rest_framework as filters

from .models import Jobs


class CharInFilter(filters.BaseInFilter, filters.CharFilter):
    ...


class JobFilterSet(filters.FilterSet):
    title = filters.CharFilter(
        field_name='title',
        lookup_expr='icontains'
    )
    company = filters.CharFilter(
        field_name='company', lookup_expr='icontains'
    )
    endereco = filters.CharFilter(
        field_name='endereco', lookup_expr='icontains'
    )
    salary_gte = filters.NumberFilter(
        field_name='salary',
        lookup_expr='gte'
    )
    salary_lte = filters.NumberFilter(
        field_name='salary',
        lookup_expr='lte'
    )

    class Meta:
        model = Jobs
        fields = {
            'title': [],
            'company': [],
            'endereco': [],
            'job_type': ['exact'],
            'job_level': ['exact'],
            'salary': []
        }
