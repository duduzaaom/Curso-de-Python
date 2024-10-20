sentence = input('Please type in a sentence: ')
index = 0

print(sentence[0])

while index <= len(sentence) - 1:
    if sentence[index - 1] == ' ':
        print(sentence[index])
    
    index += 1