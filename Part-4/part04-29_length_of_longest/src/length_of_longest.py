def length_of_longest(list):
    length_values = []

    for item in list:
        length_values.append(len(item))

        if len(item) == max(length_values):
            longest_length = len(item)

    return longest_length


if __name__ == '__main__':
    my_list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']

    print(length_of_longest(my_list))
