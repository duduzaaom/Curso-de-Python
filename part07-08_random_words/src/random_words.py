import random

def words(n: int, beginning: str) -> list:
    all_words = []

    with open('words.txt') as file:
        for line in file:
            line = line.strip()
            if line.startswith(beginning):
                all_words.append(line)

    try:
        return random.sample(all_words, n)
    except:
        raise ValueError(f'There are not enough words beginning with {beginning}.')


if __name__ == '__main__':
    word_list = words(5, "th")
    for word in word_list:
        print(word)
