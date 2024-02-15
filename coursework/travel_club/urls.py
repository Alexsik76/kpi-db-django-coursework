from django.urls import path

from .views import (
    UmlPageView,
    HomePageView,
    tourist_list
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("uml/", UmlPageView.as_view(), name="uml"),
    path("tourist_filter/", tourist_list, name="tourist-list"),
]