def even_numbers(list):
    new_list = []

    for item in list:
        if item % 2 == 0:
            new_list.append(item) 

    return new_list


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]

    new_list = even_numbers(list)
    print(list)
    print(new_list)