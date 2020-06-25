import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from django.http import HttpResponse


URL_COVID = 'https://www.worldometers.info/coronavirus/'

def top_ten(request):
    # html_page = requests.get(URL_COVID).text

    # soup = BeautifulSoup(html_page, 'lxml')

    # # Extracting the table data
    # get_table = soup.find('table', id='main_table_countries_today')

    # # From get_table. We extracted all table body and its tag 'tr'.
    # get_table_data = get_table.tbody.find_all('tr')

    # # Create a dictionary for all countries
    # dic = {}

    # for i in range(len(get_table_data)):
    #     try:
    #         key = (get_table_data[i].find_all('a', href=True)[0].string)
    #     except:
    #         key = (get_table_data[i].find_all('td')[0].string)

    # # List comprehension
    #     values = [j.string for j in get_table_data[i].find_all('td')]

    #     dic[key] = values

    #     # Print table from position 1 to all data
    # column_names = ["total-cases","new-cases", "total-deaths",
    #                 "new-deaths", "total-recovered"]

    # df = pd.DataFrame(dic).iloc[1:,1:].T.iloc[:,:5]

    # df.index_name = 'country'
    # df.columns = column_names

    # total = df.head(10).to_json()
    
    # return HttpResponse(total)

    data = {
        "total-cases": {
            "USA": "2,474,305",
            "Brazil": "1,193,609",
            "Russia": "613,994",
            "India": "481,179",
            "UK": "307,980",
            "Spain": "294,166",
            "Peru": "264,689",
            "Chile": "254,416",
            "Italy": "239,410",
            "Iran": "215,096"
        },
        "new-cases": {
            "USA": "11,751",
            "India": "8,194",
            "Russia": "7,113",
            "Mexico": "5,437",
            "Pakistan": "4,044",
            "Bangladesh": "3,946",
            "Saudi Arabia": "3,372",
            "Iran": "2,595",
            "Iraq": "2,437",
            "Oman": "1,366"
        },
        "total-deaths": {
            "USA": "124,406",
            "Brazil": "53,895",
            "UK": "43,230",
            "Italy": "34,644",
            "France": "29,731",
            "Spain": "28,327",
            "Mexico": "24,324",
            "India": "15,042",
            "Iran": "10,130",
            "Belgium": "9,726"
        },
        "new-deaths": {
            "Mexico": "947",
            "Uk": "149",
            "Pakistan": "148",
            "India": "135",
            "Iran": "134",
            "USA": "125",
            "Iraq": "107",
            "Russia": "92",
            "Indonesia": "47",
            "Saudi Arabia": "41"
        },
        "total-recovered": {
            "USA": "1,040,691",
            "Brazil": "649,908",
            "Russia": "375,164",
            "India": "277,765",
            "Chile": "215,093",
            "Italy": "186,111",
            "Germany": "176,800",
            "Iran": "175,103",
            "Turkey": "164,234",
            "Peru": "151,589"
        }
    }

    return HttpResponse(json.dumps(data))