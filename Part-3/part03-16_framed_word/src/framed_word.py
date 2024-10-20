string = input('Word: ')
blank_spaces = 30 - 2 - len(string)

print('*' * 30)
print('*' + ' ' * (blank_spaces//2) + string + ' ' * (blank_spaces - blank_spaces//2) + '*')
print('*' * 30)
