def no_vowels(string):
    vowels = 'aeiou'
    new_string = ''

    for character in string:
        if character not in vowels:
            new_string += character

    return new_string


if __name__ == '__main__':
    my_string = "this is an example"
    print(no_vowels(my_string))
