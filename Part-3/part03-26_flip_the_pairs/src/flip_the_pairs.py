number = int(input('Please type in a number: '))
current_number = 1

while current_number <= number:
    if current_number != number:
        print(current_number + 1)
    print(current_number)

    current_number += 2