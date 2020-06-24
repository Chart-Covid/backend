import requests
import bs4
import json
from django.http import HttpResponse

# It does not need pandas

# It looks for a country you enter
#country_name=input("Enter the Country name: ")

def show_countries(request, country):
    #res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    #soup = bs4.BeautifulSoup(res.text, 'lxml')
    #index = -1
    """


    """
    data=""
    print("-----------------------------")
    print("data")
    

    data_country = { 
        "country_name":country,
        "total_cases":7342359,
        "new_cases":31527,
        "total_deaths":414124,
        "new_deaths":1152,
        "total_Recovered":3619774,
        "active_cases":3308461,
    }

    print(data_country)

    return HttpResponse(json.dumps(data_country))