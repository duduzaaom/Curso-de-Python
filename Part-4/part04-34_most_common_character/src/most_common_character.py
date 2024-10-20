def most_common_character(string):
    count = 0
    most_common = ''

    for character in string:
        if string.count(character) > count:
            count = string.count(character) 
            most_common = character

    return most_common


if __name__ == '__main__':
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))