from pathlib import Path

from cities import City, CityCollection
import csv


def read_attendees_file(filepath: str = 'attendee_locations.csv') -> CityCollection:
    return ...


Cities = CityCollection(Path('attendee_locations.csv'))

print(Cities.cities[0].distance_to(Cities.cities[1]))
print(Cities.cities[0].latitude,Cities.cities[0].longitude)

print(Cities.cities[1].latitude,Cities.cities[1].longitude)
print([a.name for a in Cities.cities])

