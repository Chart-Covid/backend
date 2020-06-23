import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from django.http import HttpResponse


URL_COVID = 'https://www.worldometers.info/coronavirus/'

def top_ten(request):
    html_page = requests.get(URL_COVID).text

    soup = BeautifulSoup(html_page, 'lxml')

    # Extracting the table data
    get_table = soup.find('table', id='main_table_countries_today')

    # From get_table. We extracted all table body and its tag 'tr'.
    get_table_data = get_table.tbody.find_all('tr')

    # Create a dictionary for all countries
    dic = {}

    for i in range(len(get_table_data)):
        try:
            key = (get_table_data[i].find_all('a', href=True)[0].string)
        except:
            key = (get_table_data[i].find_all('td')[0].string)

    # List comprehension
        values = [j.string for j in get_table_data[i].find_all('td')]

        dic[key] = values

        # Print table from position 1 to all data
    column_names = ["total-cases","new-cases", "total-deaths",
                    "new-deaths", "total-recovered"]

    df = pd.DataFrame(dic).iloc[1:,1:].T.iloc[:,:5]

    df.index_name = 'country'
    df.columns = column_names

    total = df.head(10).to_json()
    
    return HttpResponse(total)