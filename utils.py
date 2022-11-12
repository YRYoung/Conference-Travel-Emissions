from pathlib import Path

from cities import City, CityCollection


def read_attendees_file(filepath: Path) -> CityCollection:
    return CityCollection(filepath)
