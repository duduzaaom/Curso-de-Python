def add_word(finnish_word: str, english_word: str):
    with open('dictionary.txt', 'a') as file:
        file.write(f'{english_word} {finnish_word}\n')


def find_word(search_term: str):
    with open('dictionary.txt') as file:
        for line in file:
            parts = line.strip().split()
            if search_term in parts[0] or search_term in parts[1]:
                print(parts[1], '-', parts[0])


def main():
    while True:
        print('1 - Add word, 2 - Search, 3 - Quit')
        function = int(input('Function: '))

        if function == 1:
            finnish_word = input('The word in Finnish: ')
            english_word = input('The word in English: ')

            add_word(finnish_word, english_word)

            print('Dictionary entry added')
        elif function == 2:
            search_term = input('Search term: ')
            find_word(search_term)
        elif function == 3:
            print('Bye!')
            break
        

main()