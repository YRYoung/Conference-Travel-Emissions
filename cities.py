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
        self.Longitude = longitude
        self.citizens_count = citizens_count
        self.name = name
        self.country = country

    def distance_to(self, other: 'City') -> float:
        raise NotImplementedError

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError


class CityCollection:
    def __init__(self, list_of_cities: List[City]):
        ...

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
