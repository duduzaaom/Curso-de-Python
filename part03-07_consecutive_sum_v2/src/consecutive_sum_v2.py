limit = int(input('Limit: '))
sum = 0
count = 0
text = 'The consecutive sum: 1 '

while sum < limit:
    count += 1
    
    if count != 1:
        text += f'+ {count} '
    sum += count

print(text + f'= {sum}')