class WeatherStation:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__observation = []

    def add_observation(self, observation: str):
        self.__observation.append(observation)

    def latest_observation(self) -> str:
        return self.__observation[-1] if self.__observation != [] else ""
    
    def number_of_observations(self) -> int:
        return len(self.__observation)
    
    def __str__(self) -> str:
        return f"{self.__name}, {len(self.__observation)} observations"
    

if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
