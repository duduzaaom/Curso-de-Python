string = input('Please type in a string: ')
last_string = len(string) - 1

while last_string >= 0:
    print(string[last_string:])
    last_string -= 1