from django.shortcuts import render
from django.views.generic.base import TemplateView

from .filters import BasePersonFilter
from .models import Tourist, Sportsman, Coach, Amateur, Person


class HomePageView(TemplateView):
    template_name = "home.html"


class UmlPageView(TemplateView):
    template_name = "diagram.html"


def tourist_list(request):
    f = BasePersonFilter(request.GET, queryset=Tourist.objects)
    return render(request, 'tourists_list.html', {'filter': f})


def trener_list(request):
    f = BasePersonFilter(request.GET, queryset=Coach.objects)
    return render(request, 'treners_list.html', {'filter': f})


def index(request):
    return render(request, 'base.html')

