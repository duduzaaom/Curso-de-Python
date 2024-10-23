class Item:
    def __init__(self, name: str, weight: float) -> None:
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"
    

class Suitcase:
    def __init__(self, maximum_weight: float) -> None:
        self.maximum_weight = maximum_weight
        self.suitcase_items = []
        self.suitcase_total_weight = 0
        
    def add_item(self, item: Item):
        if self.suitcase_total_weight + item.weight() <= self.maximum_weight:
            self.suitcase_items.append(item)
            self.suitcase_total_weight += item.weight()

    def __str__(self) -> str:
        if len(self.suitcase_items) != 1:
            return f"{len(self.suitcase_items)} items ({self.suitcase_total_weight} kg)"
        else:
            return f"{len(self.suitcase_items)} item ({self.suitcase_total_weight} kg)"
        
    def print_items(self):
        for item in self.suitcase_items:
            print(item)

    def weight(self):
        return self.suitcase_total_weight
    
    def heaviest_item(self):
        biggest_weight = 0
        heaviest_item = None
        for item in self.suitcase_items:
            if item.weight() > biggest_weight:
                biggest_weight = item.weight()
                heaviest_item = item

        return heaviest_item
    

class CargoHold:
    def __init__(self, maximum_weight: float) -> None:
        self.maximum_weight = maximum_weight
        self.current_space = maximum_weight
        self.cargohold_suitcases = []

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.suitcase_total_weight <= self.maximum_weight:
            self.cargohold_suitcases.append(suitcase)
            self.current_space -= suitcase.suitcase_total_weight

    def __str__(self) -> str:
        if len(self.cargohold_suitcases) != 1:
            return f"{len(self.cargohold_suitcases)} suitcases, space for {self.current_space} kg"
        else:
            return f"{len(self.cargohold_suitcases)} suitcase, space for {self.current_space} kg"
        
    def print_items(self):
        for suitcase in self.cargohold_suitcases:
            suitcase.print_items()
    

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()