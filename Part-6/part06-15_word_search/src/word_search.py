def read_file(filename: str) -> list:
    words = []

    with open(filename) as file:
        for line in file:
            words.append(line.strip())

    return words


def find_words(search_term: str) -> list:
    words = read_file('words.txt')
    result = []

    if '*' in search_term:
        if search_term.startswith('*'):
            for word in words:
                if word.endswith(search_term[1:]):
                    result.append(word)
        else:
            for word in words:
                if word.startswith(search_term[:-1]):
                    result.append(word)
    elif '.' in search_term:
        number_of_points = 0

        for element in search_term:
            if element == '.':
                number_of_points += 1

        for word in words:
            check = 0
            if len(word) == len(search_term):
                for index, element in enumerate(word):
                    if element == search_term[index]:
                        check += 1
                
                if check == len(search_term) - number_of_points:
                    result.append(word)
    else:
        for word in words:
            if word == search_term:
                result.append(word)

    return result


if __name__ == '__main__':
    print(find_words('.a*'))

