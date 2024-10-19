phrase = ''
previous_word = ''

while True:
    word = input('Please type in a word: ')

    if word == 'end' or word == previous_word:
        break
    else:
        phrase += word + ' '

    previous_word = word

print(phrase)