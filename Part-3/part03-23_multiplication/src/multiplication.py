limit = int(input('Please type in a number: '))
number_multiplied = 1

while number_multiplied <= limit:
    multiplier = 1

    while multiplier <= limit:
        print(f'{number_multiplied} x {multiplier} = {number_multiplied * multiplier}')
        multiplier += 1

    number_multiplied += 1
        
