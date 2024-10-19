number = int(input('How many items: '))
list = []
i = 1

while i <= number:
    item = int(input(f'Item {i}: '))

    list.append(item)
    i += 1

print(list)
