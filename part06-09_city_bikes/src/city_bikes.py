import math


def get_station_data(filename: str) -> dict:
    stations = {}

    with open(filename) as file:
        for line in file:
            parts = line.strip().split(';')
            if parts[0] == 'Longitude':
                continue
            stations[parts[3]] = (float(parts[0]), float(parts[1]))

    return stations


def distance(stations: dict, station1: str, station2: str) -> float:
    station1_longitude, station2_longitude = stations[station1][0], stations[station2][0]
    station1_latitude, station2_latitude = stations[station1][1], stations[station2][1]

    x_km = (station1_longitude - station2_longitude) * 55.26
    y_km = (station1_latitude - station2_latitude) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km


def greatest_distance(stations: dict) -> tuple:
    greatest_distance = 0
    stations_copy = stations.copy()

    for city1 in stations:
        del stations_copy[city1]
        for city2 in stations_copy:
            if distance(stations, city1, city2) > greatest_distance:
                greatest_distance = distance(stations, city1, city2)
                station1 = city1
                station2 = city2

    return station1, station2, greatest_distance


if __name__ == '__main__':
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)