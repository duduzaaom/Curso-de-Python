def math_operation(operation: str) -> int:
    if '+' in operation:
        sign = '+'
    elif '-' in operation:
        sign = '-'

    numbers = operation.split(sign)
    
    if sign == '+':
        return int(numbers[0]) + int(numbers[1])
    else:
        return int(numbers[0]) - int(numbers[1])

def filter_solutions():
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()
    lines = []

    with open('solutions.csv') as file:
        for line in file:
            number = ''
            parts = line.strip().split(';')
            lines.append(parts)

    with open('correct.csv', 'a') as file:
        for line in lines:
            if math_operation(line[1]) == int(line[2]):
                new_line = ''
                for item in line:
                    new_line += f'{item};'
                file.write(new_line[:-1] + '\n')

    with open('incorrect.csv', 'a') as file:
        for line in lines:
            if math_operation(line[1]) != int(line[2]):
                new_line = ''
                for item in line:
                    new_line += f'{item};'
                file.write(new_line[:-1] + '\n')
        

if __name__ == '__main__':
    filter_solutions()



