string = input('Please type in a string: ')
substring = input('Please type in a substring: ')

first_occurrence = string.find(substring)

if first_occurrence >= 0:
    string = string[(first_occurrence + len(substring)):]
    string = ' ' * (first_occurrence + len(substring)) + string
    #print('new string:', string)
    second_occurence = string.find(substring)

    if second_occurence >= 0:
        print(f'The second occurrence of the substring is at index {second_occurence}.')
    else:
        print('The substring does not occur twice in the string.')
else:
    print('The substring does not occur twice in the string.')
