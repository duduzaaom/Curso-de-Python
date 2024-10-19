def chessboard(length):
    vertical_length = 1

    while vertical_length <= length:
        horizontal_length = 1

        while horizontal_length <= length:
            if vertical_length % 2 != 0:
                if horizontal_length % 2 != 0:
                    if horizontal_length != length:
                        print(1, end='')
                    else:
                        print(1)
                else:
                    if horizontal_length != length:
                        print(0, end='')
                    else:
                        print(0)
            else:
                if horizontal_length % 2 != 0:
                    if horizontal_length != length:
                        print(0, end='')
                    else:
                        print(0)
                else:
                    if horizontal_length != length:
                        print(1, end='')
                    else:
                        print(1)

            horizontal_length += 1

        vertical_length += 1

if __name__ == "__main__":
    chessboard(5)
