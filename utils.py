from cities import City, CityCollection
import csv


def read_attendees_file(filepath: str = 'attendee_locations.csv') -> CityCollection:
    data = []
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:  # 将csv 文件中的数据保存到data中
            data.append(row)  # 选择某一列加入到data数组中

    cities = [City(name=data[i]['city'],
                   country=data[i]['country'],
                   citizens_count=int(data[i]['N']),
                   longitude=float(data[i]['lon']),
                   latitude=float(data[i]['lat']))

              for i in range(len(data))]

    return cities


newcity = City(name=22., country='cccccc',citizens_count= 7128, longitude=2.2,latitude= 44)
read_attendees_file()
