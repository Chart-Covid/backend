import requests
import bs4
import json
from django.http import HttpResponse


def show_countries(request, country):
    res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    data=soup.select('tr td')

    index = find_country(data,country)

    if index == -1:
        print("This country does not exist\n\n")
    else:
        dic = load_country_data(data, index)
        print_country_data(dic)


def find_country(data, country):
    if country.lower() == "world":
        country = "Total:"

    for i in range(len(data)):
        if data[i].text.lower()==country.lower():
            return i
    return -1


def load_country_data(data, index):
    dic = {'name': data[index].text,
            'total_cases': get_int(data[index+1].text),
            'new_cases': get_int(data[index+2].text),
            'tot_deaths': get_int(data[index+3].text),
            'new_deaths': get_int(data[index+4].text),
            'recovered': get_int(data[index+5].text),
            'active': get_int(data[index+6].text)}
    return dic


def get_int(str):
    s = str.strip()
    return int(s.replace(',','').replace('+','')) if s else 0

def print_country_data(country_data):
    print("Found \n")
    print(country_data['name'])
    print('=' * len(country_data['name']))

    print("Total Cases : {0:9,d}".format(country_data['total_cases']))
    print("New Cases : {0:+9,d}".format(country_data['new_cases']))

    print("Total Deaths : {0:9,d}".format(country_data['tot_deaths']))
    print("New Deaths : {0:+9,d}".format(country_data['new_deaths']))

    print("Total Recovered: {0:9,d}".format(country_data['recovered']))
    print("Active Cases : {0:9,d}".format(country_data['active']))


    return HttpResponse(json.dumps(show_countries, load_country_data, print_country_data, get_int, find_country))