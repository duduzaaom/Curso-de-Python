string = input('Please type in a string: ')
last_string = 1

while last_string <= len(string):
    print(string[:last_string])
    last_string += 1

    