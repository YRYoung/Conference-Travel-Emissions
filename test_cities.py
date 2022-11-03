import random
import string

import pytest

from cities import City


class Test_City:
    class Test_creat_new_city:
        def test_city_name(self):
            with pytest.raises(ValueError) as e:
                city = City(name=768, country='asda', citizens_count=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of city should be a string') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name=True, country='asda', citizens_count=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of city should be a string') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name=88., country='asda', citizens_count=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of city should be a string') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='bcd^S**&', country='asda', citizens_count=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of city should not contain special characters') >= 0

            number_of_strings = 5
            length_of_string = 8

            for x in range(number_of_strings):
                name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                city = City(name=name, country='asda', citizens_count=233, longitude=12.3, latitude=39)
            assert city.name == name

            pass

        def test_country_name(self):
            with pytest.raises(ValueError) as e:
                city = City(name='a', country=768, citizens_count=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of country should be a string') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country=True, citizens_count=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of country should be a string') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country=11., citizens_count=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of country should be a string') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='bcd^S**&', citizens_count=233, longitude=12.3, latitude=39)
            assert str(e.value).find('Name of country should not contain special characters') >= 0

            number_of_strings = 5
            length_of_string = 8

            for x in range(number_of_strings):
                name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
                city = City(name='a', country=name, citizens_count=233, longitude=12.3, latitude=39)
            assert city.country == name

            pass

        def test_citizens_count(self):
            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=233., longitude=12.3, latitude=39)
            assert str(e.value).find('Number of citizens should be an int') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count='aaj', longitude=12.3, latitude=39)
            assert str(e.value).find('Number of citizens should be an int') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=-2, longitude=12.3, latitude=39)
            assert str(e.value).find('Number of citizens should not be less than 1') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=0, longitude=12.3, latitude=39)
            assert str(e.value).find('Number of citizens should not be less than 1') >= 0

            for i in range(100):
                x = random.randint(1, 10000)
                city = City(name='a', country='aaa', citizens_count=x, longitude=12.3, latitude=39)
            assert city.citizens_count == x

            pass

        def test_longitude(self):
            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=233, longitude='-udisdf', latitude=39)
            assert str(e.value).find('Longitude should be float') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=233, longitude=181., latitude=39)
            assert str(e.value).find('181.0 larger than 180') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=233, longitude=-181., latitude=39)
            assert str(e.value).find('-181.0 less than -180') >= 0
            #
            city = City(name='a', country='aaa', citizens_count=233, longitude=-1, latitude=39)
            assert isinstance(city.longitude, float)
            #
            for i in range(100):
                x = random.random() * 180.
                city = City(name='a', country='aaa', citizens_count=20, longitude=x, latitude=39)
            assert city.longitude == x

            for i in range(100):
                x = - random.random() * 180.
                city = City(name='a', country='aaa', citizens_count=20, longitude=x, latitude=39)
            assert city.longitude == x

            pass

        def test_latitude(self):
            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=233, latitude='-udisdf', longitude=39)
            assert str(e.value).find('Latitude should be float') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=233, latitude=91., longitude=39)
            assert str(e.value).find('91.0 larger than 90') >= 0

            with pytest.raises(ValueError) as e:
                city = City(name='a', country='aaa', citizens_count=233, latitude=-91., longitude=39)
            assert str(e.value).find('-91.0 less than -90') >= 0
            #
            city = City(name='a', country='aaa', citizens_count=233, latitude=-1, longitude=39)
            assert isinstance(city.latitude, float)
            #
            for i in range(100):
                x = random.random() * 90.
                city = City(name='a', country='aaa', citizens_count=20, latitude=x, longitude=39)
            assert city.latitude == x

            for i in range(100):
                x = - random.random() * 90.
                city = City(name='a', country='aaa', citizens_count=20, latitude=x, longitude=39)
            assert city.latitude == x
            pass

    class Test_city_methods:
        def test_distance_to(self):
            for i in range(10000):
                long = random.random() * 360. - 180.
                lati = random.random() * 180. - 90.
                city = City(name='a', country='aaa', citizens_count=233, longitude=long, latitude=lati)
                city2 = City(name='a', country='aaa', citizens_count=233, longitude=long, latitude=lati)
                assert city.distance_to(city2) == 0.

            for i in range(10000):
                long1 = random.random() * 360. - 180.
                lati1 = random.random() * 180. - 90.
                long2 = random.random() * 360. - 180.
                lati2 = random.random() * 180. - 90.
                city1 = City(name='123', country='asda', citizens_count=233, longitude=long1, latitude=lati1)
                city2 = City(name='123', country='asda', citizens_count=233, longitude=long2, latitude=lati2)
                assert city1.distance_to(city2) == city2.distance_to(city1)

        def test_co2_to(self):
            for i in range(10000):
                long = random.random() * 360. - 180.
                lati = random.random() * 180. - 90.
                city = City(name='a', country='aaa', citizens_count=233, longitude=long, latitude=lati)
                city2 = City(name='a', country='aaa', citizens_count=233, longitude=long, latitude=lati)
                assert city.co2_to(city2) == 0.

            for i in range(10000):
                long1 = random.random() * 360. - 180.
                lati1 = random.random() * 180. - 90.
                long2 = random.random() * 360. - 180.
                lati2 = random.random() * 180. - 90.
                city1 = City(name='123', country='asda', citizens_count=233, longitude=long1, latitude=lati1)
                city2 = City(name='123', country='asda', citizens_count=233, longitude=long2, latitude=lati2)

                d = city2.distance_to(city1)
                if d <= 1000:
                    emission = 200.
                elif d <= 8000:
                    emission = 250.
                else:
                    emission = 300.

                assert city1.co2_to(city2) == city1.distance_to(city2) * emission
                assert city1.co2_to(city2) == city2.co2_to(city1)

class Test_CityCollection:
    pass

# The CityCollection methods providing simple information about the collection work correctly
# The CityCollection methods providing information about a host-city-specific metric work correctly.
# The sorted_by_emissions method works correctly.
