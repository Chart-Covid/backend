from django.urls import path
from countries import views as countries_views
from countries import top_ten
from countries import lon_lat_data

urlpatterns = [
    path('countries/top_ten/', top_ten.top_ten),
    path('countries/<str:country>', countries_views.countries_stat),
    #path('countries/', lon_lat_data.all_countries),
]
