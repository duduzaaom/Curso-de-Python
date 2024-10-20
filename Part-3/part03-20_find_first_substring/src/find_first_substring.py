word = input('Please type in a word: ')
character = input('Please type in a character: ')
first_appearance = word.find(character)

if first_appearance >= 0:
    if len(word[first_appearance:]) >= 3:
        print(word[first_appearance:(first_appearance + 3)])
