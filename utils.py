from pathlib import Path
import random

from cities import City, CityCollection


def read_attendees_file(filepath: Path) -> CityCollection:
    return CityCollection(filepath)



long = random.random() * 360. - 180.
lati = random.random() * 180. - 90.
attendees = random.randint(0, 500)
h= City(name='a 6868 56 v bjk dfgd', country='aaa', num_attendees=attendees, longitude=long, latitude=lati)


city_collection_all = CityCollection(Path('attendee_locations.csv'))
city_collection_all.summary(h)
city_collection_all.plot_top_emitters(h,save=True)