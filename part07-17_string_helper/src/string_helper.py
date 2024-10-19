from string import ascii_letters, digits

def change_case(orig_string: str) -> str:
    new_string = ''

    for character in orig_string:
        if character not in ascii_letters:
            new_string += character
            continue
        if character.isupper():
            new_string += character.lower()
        else:
            new_string += character.upper()

    return new_string


def split_in_half(orig_string: str) -> tuple:
    string_center = len(orig_string) // 2
    
    return orig_string[:string_center], orig_string[string_center:]


def remove_special_characters(orig_string: str) -> str:
    new_string = ""

    for character in orig_string:
        if character in ascii_letters or character in digits or character == " ":
            new_string += character

    return new_string


if __name__ == '__main__':
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)