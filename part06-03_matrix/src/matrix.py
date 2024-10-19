def create_matrix(matrix: list):
    with open('matrix.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split(',')
            matrix.append(line)


def matrix_sum():
    matrix = []
    sum = 0

    create_matrix(matrix)

    for row in matrix:
        for element in row:
            sum += int(element)

    return sum


def matrix_max():
    matrix = []
    create_matrix(matrix)
    start = True

    for row in matrix:
        for element in row:
            if start == True or int(element) > greatest_value:
                greatest_value = int(element)
                start = False 

    return greatest_value
        

def row_sums():
    matrix = []
    create_matrix(matrix)
    row_sum_matrix = []

    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum += int(element)
        row_sum_matrix.append(row_sum)

    return row_sum_matrix


if __name__ == '__main__':
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())


