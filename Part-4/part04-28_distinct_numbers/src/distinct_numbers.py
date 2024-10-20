def distinct_numbers(list):
    new_list = []
    list.sort()

    for item in list:
        if item in new_list:
            continue
        else:
            new_list.append(item)

    return new_list


if __name__ == '__main__':
    my_list = [3, 2, 2, 1, 3, 3, 1]

    print(distinct_numbers(my_list))
