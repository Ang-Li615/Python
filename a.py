import requests
from collections import Iterator, Iterable

def getWeather(city):
    r = requests.get('https://www.accuweather.com/en/world-weather' + city)
    data = r.json()['data']
    return '%s: %s' % (city, data)

class WeatherIterator(Iterator):
    def __init__(self,cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        else:
            city = self.cities[self.index]
            self.index = self.index + 1
            return getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

for x in WeatherIterable(['Beijing','Rome','Toronto']):
    print (x)