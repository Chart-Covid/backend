from django.urls import path
from countries import views as countries_views
from countries import top_ten

urlpatterns = [
    path('countries/', countries_views.countries_stat),
    path('top_ten/', top_ten.top_ten),
]