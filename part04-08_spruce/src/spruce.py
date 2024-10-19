def spruce(height):
    print('a spruce!')

    i = 1
    while height - i >= 0:
        print(' ' * (height - i) + '*' * i + '*' * (i - 1))

        i += 1

    print(' ' * (height - 1) + '*')

if __name__ == "__main__":
    spruce(7)