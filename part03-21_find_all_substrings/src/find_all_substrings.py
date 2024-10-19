word = input('Please type in a word: ')
character = input('Please type in a character: ')

while True:
    first_appearance = word.find(character)
    if first_appearance >= 0 and len(word[first_appearance:]) >= 3:
        print(word[first_appearance:(first_appearance + 3)])
        word = word[(first_appearance + 1):]
    else:
        break

