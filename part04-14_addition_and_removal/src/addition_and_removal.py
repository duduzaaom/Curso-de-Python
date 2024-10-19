list = []
item = 1

while True: 
    print(f'The list is now {list}')

    action = input('a(d)d, (r)emove or e(x)it: ')

    if action == 'd':
        list.append(item)
        item += 1
    elif action == 'r':
        list.remove(item - 1)
        item -= 1
    elif action == 'x':
        break

print('Bye!')