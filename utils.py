from pathlib import Path

from cities import City, CityCollection
import csv


def read_attendees_file(filepath: str = 'attendee_locations.csv') -> CityCollection:
    return ...


Cities = CityCollection(Path('attendee_locations.csv'))
countries = Cities.countries()
print(Cities.total_attendees())
