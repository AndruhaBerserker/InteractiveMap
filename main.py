import folium
import pandas as pd


data = pd.read_csv('azs.txt')
lat = data['LAT']
lon = data['LON']
name = data['NAME']
fuel = data['FUEL']


def color_azs(names):
    if name == 'Паралель':
        return 'green'
    elif name == 'Kat Oil':
        return 'orange'
    elif name == 'Авіас':
        return 'blue'
    elif name == 'Motto':
        return 'purple'
    else:
        return 'gray'


def have_fuel(fuels):
    if fuel == 'y':
        return 'gray'
    else:
        return 'red'


kram_map = folium.Map(location=[48.7301117, 37.5396764], zoom_start=12, tiles='CartoDB dark_matter')

for lat, lon, name, fuel in zip(lat, lon, name, fuel):
    folium.CircleMarker(location=[lat, lon], radius=9, popup=str(name), fill_color=color_azs(name),
                        color=have_fuel(fuel),
                        fill_opacity=0.9).add_to(kram_map)

kram_map.save('kram_map.html')

