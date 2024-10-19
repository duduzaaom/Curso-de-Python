def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    loser = {}
    smallest_value = 0

    for person in [person1, person2, person3]:
        average_value = (person["result1"] + person["result2"] + person["result3"]) / 3

        if loser == {} or average_value < smallest_value:
            loser = person
            smallest_value = average_value

    return loser


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))