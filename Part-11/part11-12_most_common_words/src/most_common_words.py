def remove_punctuation(word: str):
    if "." in word or "," in word:
        return word[:-1]
    return word


def process_file(filename: str):
    result = []
    with open(filename) as file:
        for line in file:
            result += line.strip().split()

    return [remove_punctuation(word) for word in result]


def most_common_words(filename: str, lower_limit: int):
    words = process_file(filename)

    return {word: words.count(word) for word in words if words.count(word) >= lower_limit}
    

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 4))
