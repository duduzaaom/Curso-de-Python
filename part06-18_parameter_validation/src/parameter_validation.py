def new_person(name: str, age: int) -> tuple:
    if name == '' or len(name.split()) == 1 or len(name) > 40 or age < 0 or age > 150: 
        raise ValueError()

    return name, age


if __name__ == '__main__':
    print(new_person('', 12))
