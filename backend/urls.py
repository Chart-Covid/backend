from django.urls import path
from countries import views as countries_views

urlpatterns = [
    path('countries/', countries_views.countries_stat)
]
