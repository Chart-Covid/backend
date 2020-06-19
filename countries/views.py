import requests
import json
from django.http import HttpResponse

#  URL´s to use
URL = 'https://brp.com.np/covid/country.php'
WORLD_DATA_URL = 'https://brp.com.np/covid/alldata.php'

def countries_stat(request):
    r = requests.get(WORLD_DATA_URL).json()
    
    # It fetches total cases in the world
    world_total_data = {
        'total_cases':r['total_cases'],
        'total_deaths':r['total_deaths'],
        'new_deaths':r['new_deaths'],
        'total_recovered':r['total_recovered'],
        'new_cases':r['new_cases'],
    }


    r = requests.get(URL).json()
    length = len(r['countries_stat'])
    actual_length = length + 1
    world_data = []

        # Number 14 is Mexico
    for i in range(0,14):
        r = requests.get(URL).json()

        data_covid = {
                'country_name':r['countries_stat'][i]['country_name'],
                'total_cases':r['countries_stat'][i]['cases'],
                'active_cases':r['countries_stat'][i]['active_cases'],
                'total_deaths':r['countries_stat'][i]['deaths'],
                'new_deaths':r['countries_stat'][i]['new_deaths'],
                'total_recovered':r['countries_stat'][i]['total_recovered'],
                'new_cases':r['countries_stat'][i]['new_cases'],
                'serious_critical':r['countries_stat'][i]['serious_critical']
        }

        # It fetches the country selected in range
        country_name = data_covid['country_name']
        total_cases = data_covid['total_cases']
        active_cases = data_covid['active_cases']
        total_deaths = data_covid['total_deaths']
        new_deaths = data_covid['new_deaths']
        total_recovered = data_covid['total_recovered']
        new_cases = data_covid['new_cases']
        serious_critical = data_covid['serious_critical']


        #It returns every data from a single country
    return HttpResponse(json.dumps(data_covid))
    
    
