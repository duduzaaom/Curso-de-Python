def squared(string, length):
    index = 0
    row_size = 1
    column_size = 1

    while column_size <= length:
        if row_size != length:
            print(string[index], end='')
        else:
            print(string[index])
            row_size = 0
            column_size += 1

        index += 1
        row_size += 1


        if index > len(string) - 1:
            index = 0

if __name__ == '__main__':
    squared('aybabtu', 5)
