def shortest(list):
    shortest_string = list[0]

    for string in list:
        if len(string) <= len(shortest_string):
            shortest_string = string

    return shortest_string


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)