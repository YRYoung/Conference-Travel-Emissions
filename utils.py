from pathlib import Path

from cities import City, CityCollection


def read_attendees_file(filepath: str) -> CityCollection:
    return ...


cities = CityCollection(Path('attendee_locations.csv'))

# print(cities.total_distance_travel_to(cities.cities[2]))
# print(cities.cities[0].distance_to(cities.cities[1]))
# sort_cities=cities.sorted_by_emissions()
cities.plot_top_emitters(cities.cities[100], 15, True)

# aa = cities.total_co2(cities.cities[0])
# print(cities.summary(cities.cities[0]))
