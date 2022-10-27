import csv
import math
from typing import Dict, List


class City:
    def __init__(self, name: str, country: str, citizens_count: int, longitude: float, latitude: float):
        if citizens_count < 0:
            raise Exception("Number of citizens should not be less than 0.", citizens_count)
        if latitude > 90 or latitude < -90:
            raise Exception("Invalied latitude value: " +
                            "larger than 90" if latitude > 90 else "less than -90",
                            latitude)
        if latitude > 180 or latitude < -180:
            raise Exception("Invalid longitude value: " +
                            "larger than 180" if latitude > 180 else "less than -180", longitude)
        self.latitude = latitude
        self.longitude = longitude
        self.citizens_count = citizens_count
        self.name = name
        self.country = country

    def distance_to(self, other: 'City') -> float:
        R = 6371
        return 2 * R * math.asin(
            (
                    math.sin((other.latitude - self.latitude) / 180 * math.pi / 2) ** 2 +
                    math.cos(self.latitude) * math.cos(other.latitude) *
                    math.sin((other.longitude - self.longitude) / 180 * math.pi / 2) ** 2
            ) ** .5)

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError


def read_csv(filepath: str):
    data = []
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  # 将csv 文件中的数据保存到data中
            data.append(row)  # 选择某一列加入到data数组中

    return [City(name=data[i]['city'],
                 country=data[i]['country'],
                 citizens_count=int(data[i]['N']),
                 longitude=float(data[i]['lon']),
                 latitude=float(data[i]['lat']))
            for i in range(len(data))]


class CityCollection:
    def __init__(self, input):
        self.cities = input if isinstance(input, list) else read_csv(input)

    def countries(self) -> List[str]:
        raise NotImplementedError

    def total_attendees(self) -> int:
        raise NotImplementedError

    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[City]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError
