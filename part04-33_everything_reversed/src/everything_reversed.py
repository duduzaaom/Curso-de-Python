def everything_reversed(list):
    new_list = []

    for string in list:
        string = string[::-1]
        
        new_list.append(string)

    new_list_reversed = new_list[::-1]

    return new_list_reversed


if __name__ == '__main__':
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
