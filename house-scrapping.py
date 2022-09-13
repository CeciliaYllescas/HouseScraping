from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd

url = "https://inmuebles.mercadolibre.com.ar/alquiler/3-ambientes/bsas-gba-norte/san-fernando/alquiler_NoIndex_True#applied_filter_id%3DROOMS%26applied_filter_name%3DAmbientes%26applied_filter_order%3D9%26applied_value_id%3D%5B3-3%5D%26applied_value_name%3D3+ambientes%26applied_value_order%3D3%26applied_value_results%3D16%26is_custom%3Dfalse"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

titulos= []
ubicaciones=[]
precios= []
areas = []

for lista in soup.find_all('li',class_="ui-search-layout__item"):
    casas = lista

    for casa in casas:
        title = casas.find('h2', class_="ui-search-item__title").text.replace('\n', '')
        titulos.append(title)

        location = casas.find('span', class_="ui-search-item__location").text.replace('\n', '')
        ubicaciones.append(location)

        price = casas.find('span', class_="price-tag-amount").text.replace('\n', '')
        precios.append(price)

        area = casas.find('li', class_="ui-search-card-attributes__attribute").text.replace('\n', '')
        areas.append(area)


    MyDict = { 'Título': titulos, 
    'Ubicación': ubicaciones, 
    'Precio': precios, 
    'Area': areas
    }

    datacasas = pd.DataFrame(MyDict)
    datacasas.to_csv('datacasas.csv', index=False, encoding='utf-8')
    print (datacasas)

        