limit = int(input('Limit: '))
sum = 0
count = 0

while sum < limit:
    count += 1
    #print('Count =', count)
    sum += count
    #print('Sum =', sum)

print(sum)
