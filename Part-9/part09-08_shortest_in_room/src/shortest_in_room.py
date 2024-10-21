class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        line = ""
        total_height = 0
        for person in self.persons:
            line += f"{person.name} ({person.height} cm)\n"
            total_height += person.height

        print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
        print(line[:-2])

    def shortest(self):
        shortest_height = 0
        for person in self.persons:
            if person.height < shortest_height or shortest_height == 0:
                shortest_height = person.height
                shortest_person = person
            
        return shortest_person if self.persons != [] else None
    
    def remove_shortest(self):
        if len(self.persons) > 0:  
            shortest_person = self.shortest()
            self.persons.remove(shortest_person)
            return shortest_person
        return None 


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()