import csv
import math
from typing import Dict, List

import matplotlib.pyplot as plt

illegal_string = "~!@#$%^&*()_+-*/<>,.[]\/"


def read_csv(filepath: str):
    data = []
    with open(filepath, 'r', newline='', encoding="utf8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  # 将csv 文件中的数据保存到data中
            data.append(row)  # 选择某一列加入到data数组中

    return [City(name=data[i]['city'],
                 country=data[i]['country'],
                 citizens_count=int(data[i]['N']),
                 longitude=float(data[i]['lon']),
                 latitude=float(data[i]['lat']))
            for i in range(len(data))]


class City:

    def __init__(self, name: str, country: str, citizens_count: int, longitude: float, latitude: float):
        self.latitude = latitude
        self.longitude = longitude
        self.citizens_count = citizens_count
        self.name = name
        self.country = country

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name of city should be a string instead of {}".format(type(value)))
        for i in illegal_string:
            if value.find(i) >= 0:
                raise ValueError("Name of city should not contain special characters")
        self._name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if not isinstance(value, str):
            raise TypeError("Name of country should be a string instead of {}".format(type(value)))
        for i in illegal_string:
            if value.find(i) >= 0:
                raise ValueError("Name of country should not contain special characters")
        self._country = value

    @property
    def citizens_count(self):
        return self._citizens_count

    @citizens_count.setter
    def citizens_count(self, value):
        if not isinstance(value, int):
            raise TypeError("Number of citizens should be an int instead of {}".format(type(value)))
        if value <= 0:
            raise ValueError("Number of citizens should not be less than 1")
        self._citizens_count = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError(
                "Latitude should be float instead of {}".format(type(value)))

        if value > 90 or value < -90:
            raise ValueError("Invalid latitude value: {} {} than {}".format
                             (value,
                              'larger' if value > 90 else 'less',
                              90 if value > 90 else -90)
                             )
        self._latitude = float(value)

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError(
                "Longitude should be float instead of {}".format(type(value)))
        if value > 180 or value < -180:
            raise ValueError("Invalid longitude value: {} {} than {}".format
                             (value,
                              'larger' if value > 180 else 'less',
                              180 if value > 180 else -180))
        self._longitude = float(value)

    def distance_to(self, other: 'City') -> float:
        R = 6371
        return 2 * R * math.asin(
            (
                    math.sin((other.latitude - self.latitude) / 180 * math.pi / 2) ** 2 +
                    math.cos(self.latitude / 180 * math.pi) * math.cos(other.latitude / 180 * math.pi) *
                    math.sin((other.longitude - self.longitude) / 180 * math.pi / 2) ** 2
            ) ** .5)

    def co2_to(self, other: 'City') -> float:
        d = self.distance_to(other)
        if d <= 1000:
            emission = 200.
        elif d <= 8000:
            emission = 250.
        else:
            emission = 300.
        return emission * d


class CityCollection:
    def __init__(self, value):
        self.cities = value

    def __len__(self):
        return len(self._cities)

    @property
    def cities(self):
        return self._cities

    @cities.setter
    def cities(self, value):
        if isinstance(value, list):
            self._cities = value
        elif str(type(value)).find('Path') >= 0:
            self._cities = read_csv(value)

        for i in illegal_string:
            if value.find(i) >= 0:
                raise ValueError("Name of city should not contain special characters")

    def countries(self) -> List[str]:
        countries = [city.country for city in self.cities]
        countries = list(set(countries))
        return countries

    def total_attendees(self) -> int:
        total = 0
        for city in self.cities:
            total += city.citizens_count
        return total

    def total_distance_travel_to(self, city: City) -> float:
        total_d = 0.
        for c in self.cities:
            total_d += c.distance_to(city) * c.citizens_count
        return total_d

    def travel_by_country(self, city: City) -> Dict[str, float]:
        dict = {}
        countries = self.countries()
        for country in countries:
            cities_of_a_country = CityCollection([c for c in self.cities if c.country == country])
            # for c in cities_of_a_country.cities: assert c.country == country
            dict[country] = cities_of_a_country.total_distance_travel_to(city)
        return dict

    def total_co2(self, city: City) -> float:
        total = 0
        for c in self.cities:
            total += c.co2_to(city) * c.citizens_count
        return total

    def co2_by_country(self, city: City) -> Dict[str, float]:
        dict = {}
        countries = self.countries()
        for country in countries:
            cities_of_a_country = CityCollection([c for c in self.cities if c.country == country])
            # for c in cities_of_a_country.cities: assert c.country == country
            dict[country] = cities_of_a_country.total_co2(city)
        return dict

    def summary(self, city: City):
        print('Host city: {} ({})'.format(city.name, city.country))
        print('Total CO2: {} tones'.format(round(self.total_co2(city) / 1000.)))
        print('Total attendees travelling to Zurich from {} different cities: {}'.format(
            self.__len__(), self.total_attendees()))
        return

    def sorted_by_emissions(self) -> List[City]:
        sort_list = self.cities.copy()
        sort_list.sort(key=lambda h_city: self.total_co2(h_city), reverse=True)
        # for i in range(len(sort_list) - 1):
        #     print(i)
        #     assert self.total_co2(sort_list[i]) >= self.total_co2(sort_list[i + 1])
        return sort_list

    def plot_top_emitters(self, city: City, n: int = 10, save: bool = False):
        countries_dict = self.co2_by_country(city)
        countries_emissions_list = [(country_name, countries_dict[country_name]) for country_name in
                                    countries_dict.keys()]

        countries_emissions_list.sort(key=lambda tuple: tuple[1], reverse=True)

        emissions_everywhere_else = 0
        for tuple in countries_emissions_list[n:]:
            emissions_everywhere_else += tuple[1]

        new_list = countries_emissions_list[:n] + [('All other countries', emissions_everywhere_else)]

        names = [item[0] for item in new_list]
        emissions = [item[1] / 1000 for item in new_list]

        plt.figure(figsize=(n * 1.5, n))
        plt.title('Total Emissions from Each Country (top {})'.format(n))
        plt.ylabel('Total emissions(tonnes CO2)')
        plt.bar(names, emissions, color=['royalblue', 'hotpink'])

        if save:
            plt.savefig(city.name.replace(' ', '_') + '.png')

        plt.show()
