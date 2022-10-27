from pathlib import Path

from cities import City, CityCollection
import csv


def read_attendees_file(filepath: str = 'attendee_locations.csv') -> CityCollection:


    return ...


Cities=CityCollection(Path('attendee_locations.csv'))
Cities2=CityCollection(Cities.cities)

print(Cities.cities)

