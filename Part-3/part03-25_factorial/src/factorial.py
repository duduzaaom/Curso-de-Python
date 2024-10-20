while True:
    number = int(input('Please type in a number: '))
    current_multiplier = 1
    factorial = 1

    if number <= 0:
        break

    while current_multiplier <= number:
        factorial *= current_multiplier
        current_multiplier += 1

    print(f'The factorial of the number {number} is {factorial}')

print('Thanks and bye!')

