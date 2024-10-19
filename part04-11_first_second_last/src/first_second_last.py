def first_word(sentence):
    index = 0

    while True:
        if sentence[index] == ' ':
            return sentence[:index]

        index += 1


def second_word(sentence):
    index = 0
    empty_occurrence = 0

    while True:
        if sentence[index] == ' ':
            empty_occurrence += 1
            if empty_occurrence == 2:
                return sentence[(empty_occurrence_index + 1):index]
            empty_occurrence_index = index

        if empty_occurrence == 1 and index == len(sentence) - 1:
            return sentence[(empty_occurrence_index + 1):]

        index += 1


def last_word(sentence):
    index = 0

    while True:
        if sentence[index] == ' ':
            empty_occurrence_index = index

        if index == len(sentence) - 1:
            return sentence[(empty_occurrence_index + 1):]

        index += 1
            

if __name__ == "__main__":
    sentence = "Eduardo Augusto Lima de Araújo"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))