while True:
    string = input('Please type in a string: ')

    if len(string) == 0:
        break
    else: 
        print(string)
        print('-' * len(string))