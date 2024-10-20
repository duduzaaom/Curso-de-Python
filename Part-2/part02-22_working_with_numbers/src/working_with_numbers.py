print('Please type in integer numbers. Type in 0 to finish.')
count = 0
sum = 0
negatives = 0
positives = 0

while True:
    number = int(input('Number: '))
    count += 1

    if number == 0:
        count -= 1
        break
    else:
        sum += number
        if number < 0:
            negatives += 1
        else:
            positives += 1

mean = sum/count

print(f'Numbers typed in {count}')
print(f'The sum of the numbers is {sum}')
print(f'The mean of the numbers is {mean}')
print(f'Positive numbers {positives}')
print(f'Negative numbers {negatives}')