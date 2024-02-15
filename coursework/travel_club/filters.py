import django_filters
from .models import Tourist, Section, Group


class TouristFilter(django_filters.FilterSet):
    birth_date = django_filters.DateFilter(field_name='birth_date', lookup_expr='gte')
    group = django_filters.ModelChoiceFilter(queryset=Group.objects, field_name='group', lookup_expr='exact')
    class Meta:

        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'group']
