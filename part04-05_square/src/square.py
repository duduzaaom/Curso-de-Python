def line(length, string):
    if string != '':
        print(string[0] * length)
    else:
        print('*' * length)


def square(size, character):
    i = 1

    while i <= size:
        line(size, character)

        i += 1


if __name__ == "__main__":
    square(4, "^")