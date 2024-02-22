from django.shortcuts import render
from django.views.generic.base import TemplateView

from .filters import TouristFilter, CoachFilter
from .models import Tourist, Sportsman, Coach, Amateur, Person


class HomePageView(TemplateView):
    template_name = "home.html"


class UmlPageView(TemplateView):
    template_name = "diagram.html"


def tourist_list(request):
    field_list = ['first_name', 'last_name', 'gender', 'birth_date']
    tourists = Tourist.objects.values_list(*field_list)
    f = TouristFilter(request.GET, queryset=tourists.all())
    return render(request, 'tourists_list.html', {'filter': f})


def trener_list(request):
    field_list = ['first_name', 'last_name', 'gender', 'birth_date', 'salary', 'spec']
    tourists = Coach.objects.values_list(*field_list)
    f = CoachFilter(request.GET, queryset=tourists.all())
    return render(request, 'treners_list.html', {'filter': f})


def index(request):
    return render(request, 'base.html')

