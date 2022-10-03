import os
import json
from statistics import mean
from pprint import pprint
from lxml import etree

path = './source_data'
cities = dict.fromkeys(sorted(os.listdir(path)))

for city in cities:
    with open(path + '/' + city + '/2021_09_25.json') as file:
        data = json.load(file)

    data_hourly = data['hourly']

    temps = [hour['temp'] for hour in data_hourly]
    wind_speeds = [hour['wind_speed'] for hour in data_hourly]

    result = {'mean_temp': mean(temps), 'mean_wind_speed': mean(wind_speeds),
              'min_temp': min(temps), 'min_wind_speed': min(wind_speeds),
              'max_temp': max(temps), 'max_wind_speed': max(wind_speeds)}

    result = {key: round(value, 2) for key, value in result.items()}

    cities[city] = result

pprint(cities)

coldest_place = ''
warmest_place = ''
windiest_place = ''
min_temp = 999
max_temp = -999
max_wind_speed = -999
for city, values in cities.items():
    if values['mean_temp'] < min_temp:
        min_temp = values['mean_temp']
        coldest_place = city
    if values['mean_temp'] > max_temp:
        max_temp = values['mean_temp']
        warmest_place = city
    if values['mean_wind_speed'] > max_wind_speed:
        max_wind_speed = values['mean_wind_speed']
        windiest_place = city

# coldest = min([values['mean_temp'] for values in cities.values()])
# print(coldest)
'''
'coldest_place': {str(value): key for key, value in cities.items()}.get(
                       str(min([values['mean_temp'] for values in cities.values()]))
                   ),
'''

summary_attribs = {'mean_temp': round(mean([values['mean_temp'] for values in cities.values()]), 2),
                   'mean_wind_speed': round(mean([values['mean_wind_speed'] for values in cities.values()]), 2),
                   'coldest_place': coldest_place,
                   'warmest_place': warmest_place,
                   'windiest_place': windiest_place}

weather = etree.Element('weather', {'country': 'Spain', 'date': '2021-09-25'})
summary = etree.SubElement(weather, 'summary', {key: str(value) for key, value in summary_attribs.items()})
cities_xml = etree.SubElement(weather, 'cities')
for city, values in cities.items():
    etree.SubElement(cities_xml, city.replace(' ', '_'), {key: str(value) for key, value in values.items()})

xml_str = etree.tostring(weather, pretty_print=True)

with open('result.xml', 'wb') as result_file:
    result_file.write(xml_str)
