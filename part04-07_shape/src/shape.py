def line(length, string):
    if string != '':
        print(string[0] * length)
    else:
        print('*' * length)


def shape(length, character1, height, character2):
    i = 1

    while i <= length:
        line(i, character1)

        i += 1

    i = 1

    while i <= height:
        line(length, character2)

        i += 1

if __name__ == "__main__":
    shape(5, "x", 2, "o")