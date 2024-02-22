import django_filters
from .models import Tourist, Section, Group, Coach


class TouristFilter(django_filters.FilterSet):
    birth_date = django_filters.DateFilter(field_name='birth_date', lookup_expr='gte')
    group = django_filters.ModelChoiceFilter(queryset=Group.objects.all(), field_name='group', lookup_expr='exact')
    section = django_filters.ModelChoiceFilter(queryset=Section.objects.all(), field_name='group__section', lookup_expr='exact')
    gender = django_filters.ChoiceFilter(field_name='gender', choices=( (1, "чоловік"),(2, "жінка")))

    class Meta:
        model = Tourist
        fields = ['gender', 'birth_date', 'group', 'section']

class CoachFilter(django_filters.FilterSet):
    section = django_filters.ModelChoiceFilter(queryset=Section.objects.all(), field_name='group__section',
                                               lookup_expr='exact')
    class Meta:
        model = Coach
        fields = ['gender', 'birth_date', 'group', 'spec', 'salary']