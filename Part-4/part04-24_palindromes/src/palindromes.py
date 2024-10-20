def palindromes(string : str):
    new_string = ''

    for index in range(len(string) - 1, -1, -1):
        new_string += string[index]

    return string == new_string


while True:
    word = input('Please type in a palindrome: ')

    if palindromes(word):
        print(f'{word} is a palindrome!')
        break
    else:
        print("that wasn't a palindrome")

