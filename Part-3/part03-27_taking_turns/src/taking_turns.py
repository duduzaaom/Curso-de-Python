number = int(input('Please type in a number: '))
number_copy = number
current_number = 1
count = 1

while count <= number//2:
    print(current_number)
    print(number_copy)

    current_number += 1
    count += 1
    number_copy -= 1

if number % 2 != 0:
    print(number//2 + 1)

