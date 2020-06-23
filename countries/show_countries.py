import requests
import bs4
import json
from django.http import HttpResponse

# It does not need pandas

# It looks for a country you enter
<<<<<<< Updated upstream
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
=======
# country_name=input("Enter the Country name: ")

def show_countries(requests, country):
    res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    index = -1
    data=soup.select('tr td')
    for i in range(len(data)):
        if data[i].text.lower()==country.lower():
            index=i
            break

    for i in range(7):
        if i == 0:
            print("\nCountry name: "+str(data[i+index].text))
        elif i == 1:
            print("Total cases: "+str(data[i+index].text))
        elif i == 2:
            if data[i+index].text == '':
                print("New cases: 0")
            else:
                print("New cases: "+str(data[i+index].text))
        elif i == 3:
            print("Total deaths: "+str(data[i+index].text))
        elif i == 4:
            if data[i+index].text == '':
                print("New deaths: 0")
            else:
                print("New deaths: "+str(data[i+index].text))
        elif i == 5:
            print("Total Recovered: "+str(data[i+index].text))
        elif i == 6:
            print("Active cases: "+str(data[i+index].text),end='\n\n')

        print(country)
        
# show_countries(country_name)
>>>>>>> Stashed changes
