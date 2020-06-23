from django.urls import path
from countries import views as countries_views
from countries import top_ten, lon_lat_data, show_countries


urlpatterns = [
    #path('show_countries/', show_countries.show_countries),
    path('top_ten/', top_ten.top_ten),
    path('countries/<str:country>/', show_countries.show_countries),
    #path('countries/', lon_lat_data.all_countries),
]
