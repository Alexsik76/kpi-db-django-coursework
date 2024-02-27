import django_filters
from .models import Tourist, Section, Group, Coach
from django.utils import timezone
from dateutil.relativedelta import relativedelta


def filter_age(queryset, name, value):
    date = timezone.now().date() - relativedelta(years=value)
    lookup = '__'.join([name, 'lte'])
    return queryset.filter(**{lookup: date})


class BasePersonFilter(django_filters.FilterSet):
    # birth_date = django_filters.DateFilter(field_name='birth_date', lookup_expr='gte')
    group = django_filters.ModelChoiceFilter(queryset=Group.objects.all(), field_name='group',label='Група', lookup_expr='exact')
    section = django_filters.ModelChoiceFilter(queryset=Section.objects.all(), label='Секція', field_name='group__section',
                                               lookup_expr='exact')
    gender = django_filters.ChoiceFilter(field_name='gender',label='Стать', choices=((1, "чоловік"), (2, "жінка")))
    age = django_filters.NumberFilter(field_name='birth_date', label="Старше ніж", method=filter_age)


