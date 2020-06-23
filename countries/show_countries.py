import requests
import bs4
import json
from django.http import HttpResponse

# It does not need pandas

# It looks for a country you enter
#country_name=input("Enter the Country name: ")

def show_countries(request, country):
    res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    index = -1
    """


    """
    data=""
    print("-----------------------------")
    print("data")
    

    data_country = {
        "country_name":country,
        "total_cases":country,
        "new_cases":country,
        "total_deaths":country,
        "new_deaths":country,
        "total_Recovered":country,
        "active_cases":country,
    }

    print(data_country)

    return HttpResponse(json.dumps(data_country))