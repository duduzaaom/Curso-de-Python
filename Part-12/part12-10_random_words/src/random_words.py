import random

def random_words(characters: str, length: int):
        word = ""
        for i in range(length):
            word += random.choice(characters)

        return word


def word_generator(characters: str, length: int, amount: int):
    return (random_words(characters, length) for i in range(amount))


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)