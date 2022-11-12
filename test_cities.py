import random
import string
from pathlib import Path

import pytest

from cities import City, CityCollection


def generate_random_city():
    long = random.random() * 360. - 180.
    lati = random.random() * 180. - 90.
    attendees = random.randint(0, 500)
    return City(name='a', country='aaa', num_attendees=attendees, longitude=long, latitude=lati)


class Test_City:
    class Test_creat_new_city:
        def test_city_name(self):
            with pytest.raises(TypeError) as e:
                city = City(name=768, country='asda', num_attendees=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of city should be a string') >= 0

            with pytest.raises(TypeError) as e:
                city = City(name=True, country='asda', num_attendees=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of city should be a string') >= 0

            with pytest.raises(TypeError) as e:
                city = City(name=88., country='asda', num_attendees=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of city should be a string') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='bcd^S**&', country='asda', num_attendees=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of city should not contain special characters') >= 0

            number_of_strings = 5
            length_of_string = 8

            for x in range(number_of_strings):
                name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                city = City(name=name, country='asda', num_attendees=233, longitude=12.3, latitude=39)
            assert city.name == name

            pass

        def test_country_name(self):
            with pytest.raises(TypeError) as e:
                city = City(name='a', country=768, num_attendees=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of country should be a string') >= 0

            with pytest.raises(TypeError) as e:
                city = City(name='a', country=True, num_attendees=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of country should be a string') >= 0

            with pytest.raises(TypeError) as e:
                city = City(name='a', country=11., num_attendees=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of country should be a string') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='bcd^S**&', num_attendees=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of country should not contain special characters') >= 0

            number_of_strings = 5
            length_of_string = 8

            for x in range(number_of_strings):
                name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                city = City(name='a', country=name, num_attendees=233, longitude=12.3, latitude=39)
            assert city.country == name

            pass

        def test_citizens_count(self):
            with pytest.raises(TypeError) as e:
                city = City(name='a', country='aaa', num_attendees=233., longitude=12.3, latitude=39)
            assert str(e.value).find('Number of citizens should be an int') >= 0

            with pytest.raises(TypeError) as e:
                city = City(name='a', country='aaa', num_attendees='aaj', longitude=12.3, latitude=39)
            assert str(e.value).find('Number of citizens should be an int') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', num_attendees=-2, longitude=12.3, latitude=39)
            assert str(e.value).find('Number of citizens should not be less than 1') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', num_attendees=0, longitude=12.3, latitude=39)
            assert str(e.value).find('Number of citizens should not be less than 1') >= 0

            for i in range(100):
                x = random.randint(1, 10000)
                city = City(name='a', country='aaa', num_attendees=x, longitude=12.3, latitude=39)
            assert city.num_attendees == x

            pass

        def test_longitude(self):
            with pytest.raises(TypeError) as e:
                city = City(name='a', country='aaa', num_attendees=233, longitude='-udisdf', latitude=39)
            assert str(e.value).find('Longitude should be float') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', num_attendees=233, longitude=181., latitude=39)
            assert str(e.value).find('181.0 larger than 180') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', num_attendees=233, longitude=-181., latitude=39)
            assert str(e.value).find('-181.0 less than -180') >= 0
            #
            city = City(name='a', country='aaa', num_attendees=233, longitude=-1, latitude=39)
            assert isinstance(city.longitude, float)
            #
            for i in range(100):
                x = random.random() * 180.
                city = City(name='a', country='aaa', num_attendees=20, longitude=x, latitude=39)
            assert city.longitude == x

            for i in range(100):
                x = - random.random() * 180.
                city = City(name='a', country='aaa', num_attendees=20, longitude=x, latitude=39)
            assert city.longitude == x

            pass

        def test_latitude(self):
            with pytest.raises(TypeError) as e:
                city = City(name='a', country='aaa', num_attendees=233, latitude='-udisdf', longitude=39)
            assert str(e.value).find('Latitude should be float') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', num_attendees=233, latitude=91., longitude=39)
            assert str(e.value).find('91.0 larger than 90') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', num_attendees=233, latitude=-91., longitude=39)
            assert str(e.value).find('-91.0 less than -90') >= 0
            #
            city = City(name='a', country='aaa', num_attendees=233, latitude=-1, longitude=39)
            assert isinstance(city.latitude, float)
            #
            for i in range(100):
                x = random.random() * 90.
                city = City(name='a', country='aaa', num_attendees=20, latitude=x, longitude=39)
            assert city.latitude == x

            for i in range(100):
                x = - random.random() * 90.
                city = City(name='a', country='aaa', num_attendees=20, latitude=x, longitude=39)
            assert city.latitude == x
            pass

    class Test_city_methods:
        def test_distance_to(self):
            for i in range(10000):
                city = generate_random_city()
                city2 = City(name='a', country='aaa', num_attendees=233, longitude=city.longitude,
                             latitude=city.latitude)
                assert city.distance_to(city2) == 0.

            for i in range(10000):
                city1 = generate_random_city()
                city2 = generate_random_city()
                assert city1.distance_to(city2) == city2.distance_to(city1)

        def test_co2_to(self):
            for i in range(10):
                city = generate_random_city()
                city2 = City(name='a', country='aaa', num_attendees=233, longitude=city.longitude,
                             latitude=city.latitude)
                assert city.co2_to_per_person(city2) == 0.

            for i in range(10000):
                city1 = generate_random_city()
                city2 = generate_random_city()

                d = city2.distance_to(city1)
                if d <= 1000:
                    emission = 200.
                elif d <= 8000:
                    emission = 250.
                else:
                    emission = 300.

                assert city1.co2_to_per_person(city2) == city1.distance_to(city2) * emission
                assert city1.co2_to_per_person(city2) == city2.co2_to_per_person(city1)

                assert abs(city1.co2_to(city2) - city1.distance_to(city2) * city1.num_attendees * emission) < 0.0001
                assert abs(city2.co2_to(city1) - city2.distance_to(city1) * city2.num_attendees * emission) < 0.0001


city_collection_all = CityCollection(Path('attendee_locations.csv'))
city_collection = CityCollection(random.sample(city_collection_all.cities, 400))


class Test_CityCollection:
    class Test_simple_info:
        def test_countries(self):
            for i in range(0, len(city_collection)):
                sub_city_collection = CityCollection(city_collection.cities[:i])

                countries = sub_city_collection.countries()
                for city in sub_city_collection.cities:
                    assert countries.count(city.country) == 1

        def test_total_attendees(self):
            for i in range(0, len(city_collection)):
                sub_city_collection = CityCollection(city_collection.cities[:i])
                total = sub_city_collection.total_attendees()
                for city in sub_city_collection.cities:
                    total -= city.num_attendees
                assert total == 0

    class Test_host2cities_methods:
        def test_total_distance_travel_to(self):

            for i in range(10):
                random_city = generate_random_city()

                for i in range(0, len(city_collection) - 1):
                    sub_city_collection_1 = CityCollection(city_collection[:i])
                    sub_city_collection_2 = CityCollection(city_collection[i:])
                    assert -0.00001 < sub_city_collection_1.total_distance_travel_to(
                        random_city) + sub_city_collection_2.total_distance_travel_to(
                        random_city) - city_collection.total_distance_travel_to(random_city) < 0.00001

        def test_travel_by_country(self):

            for i in range(1, len(city_collection)):
                sub_city_collection = CityCollection(city_collection.cities[:i])

                random_city = generate_random_city()

                countries_dict = sub_city_collection.travel_by_country(random_city)
                # test if the keys include all countries
                assert set(countries_dict.keys()) == set(sub_city_collection.countries())

                # test if the sum of distances of countries == total distance
                total_dist = 0.
                for value in countries_dict.values():
                    total_dist += value
                assert abs(total_dist - sub_city_collection.total_distance_travel_to(random_city)) < 0.00001

        def test_total_co2(self):

            for i in range(10):
                random_city = generate_random_city()
                for i in range(0, len(city_collection) - 1):
                    sub_city_collection_1 = CityCollection(city_collection[:i])
                    sub_city_collection_2 = CityCollection(city_collection[i:])
                    assert abs(sub_city_collection_1.total_co2(
                        random_city) + sub_city_collection_2.total_co2(
                        random_city) - city_collection.total_co2(random_city)) < 0.001

            pass

        def test_co2_by_country(self):

            for i in range(1, len(city_collection)):
                sub_city_collection = CityCollection(city_collection.cities[:i])
                random_city = generate_random_city()

                countries_dict = sub_city_collection.co2_by_country(random_city)
                # test if the keys include all countries
                assert set(countries_dict.keys()) == set(sub_city_collection.countries())

                # test if the sum of emission of countries == total emission
                total_emission = 0.
                for value in countries_dict.values():
                    total_emission += value
                assert abs(total_emission - sub_city_collection.total_co2(random_city)) < 0.001

    def test_sort(self):
        for i in range(6, len(city_collection)):
            sub_city_collection = CityCollection(city_collection.cities[:i])

            hosts = sub_city_collection.sorted_by_emissions()
            for i in range(len(hosts) - 1):
                assert hosts[i][1] >= hosts[i + 1][1]
